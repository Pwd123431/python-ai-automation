import os
import sqlite3
import PyPDF2
import requests
import json
import time

api_url = "https://api.deepseek.com/chat/completions"
api_key = "sk-fde4e297a9064baab0292addeeb9404c" # 👈 务必换掉！！！

pdf_folder = "./02_data/biochar_pdfs/"
db_path = "./02_data/ai_project_v2.db" # 👈 我们换一个全新的数据库名字，绕过所有历史遗留问题！

# 1. 连接数据库
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 2. 建一张完美的新表（直接带上 filename 列）
cursor.execute('''
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT UNIQUE,
        title TEXT,
        keywords TEXT,
        abstract TEXT
    )
''')
conn.commit()

# 3. 获取文件夹里所有的文件
all_files = os.listdir(pdf_folder)
pdf_files = [f for f in all_files if f.endswith('.pdf')]
print(f"📁 文件夹里共找到 {len(pdf_files)} 篇 PDF 论文。")

# 4. 开始循环
for index, filename in enumerate(pdf_files):
    # 检查是否处理过
    cursor.execute("SELECT id FROM documents WHERE filename = ?", (filename,))
    if cursor.fetchone():
        print(f"⏭️ 跳过已处理过的文件: {filename}")
        continue

    file_path = os.path.join(pdf_folder, filename)
    print(f"\n========== [{index+1}/{len(pdf_files)}] 正在处理: {filename} ==========")

    # 读取前两页
    try:
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            pdf_text = ""
            for i in range(min(2, len(reader.pages))):
                pdf_text += reader.pages[i].extract_text() + "\n"
    except Exception as e:
        print(f"❌ 读取 PDF 失败，跳过此文件。错误信息: {e}")
        continue

    # 发送给 AI 提取（这次加了 400 字要求和 max_tokens）
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "你是一个专业的学术翻译和总结专家。"},
            {"role": "user", "content": f"请从以下论文文本中提取信息。必须返回 JSON 格式。包含三个键：'title'（英文标题），'keywords'（3个英文关键词的列表），'abstract'（400字左右的中文详细摘要，不要只写一两句，必须包含研究背景、制备方法、核心结论等）。文本：{pdf_text}"}
        ],
        "response_format": {"type": "json_object"},
        "max_tokens": 2000
    }

    try:
        res = requests.post(api_url, headers=headers, json=payload, timeout=40)
        
        if res.status_code == 200:
            ai_text = res.json()["choices"][0]["message"]["content"]
            data = json.loads(ai_text)
            
            # 存入库
            keywords_str = ", ".join(data["keywords"])
            cursor.execute(
                "INSERT INTO documents (filename, title, keywords, abstract) VALUES (?, ?, ?, ?)", 
                (filename, data["title"], keywords_str, data["abstract"])
            )
            conn.commit()
            print(f"✅ 提取成功并已入库: {data['title'][:40]}...")
            
        else:
            print(f"❌ AI 接口报错，状态码: {res.status_code}")
            print(res.text)
            
    except Exception as e:
        print(f"❌ 请求或解析时发生异常: {e}")

    # 每次处理完休息 3 秒
    time.sleep(3)

conn.close()
print("\n🎉 所有论文批量处理完毕！")