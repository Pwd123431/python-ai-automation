import sqlite3
import PyPDF2
import requests
import json
import time

#读取pdf
with open("./02_data/test.pdf",'rb') as f:
    reader=PyPDF2.PdfReader(f)

    #读取第一页
    page=reader.pages[0]
    pdf_text=page.extract_text()
print("pdf读取成功，长度：",len(pdf_text))


api_url = "https://api.deepseek.com/chat/completions"
api_key = "sk-fde4e297a9064baab0292addeeb9404c" # 👈 务必换掉

conn = sqlite3.connect("./02_data/ai_project.db")
cursor = conn.cursor()

# 1. 先清空之前搞乱的脏数据，防止干扰测试 (把 abstract 全部设为空，让程序重新跑)
cursor.execute("UPDATE documents SET abstract = NULL")
conn.commit()

# 2. 查出需要生成摘要的文章（只需要查 id 和 title 就够了）
cursor.execute("SELECT id, title FROM documents WHERE abstract IS NULL")
docs = cursor.fetchall()
print(f"找到 {len(docs)} 篇需要生成摘要的论文。")

# 3. 循环处理
for doc_id, title in docs:
    print(f"\n正在处理: {title[:30]}...")
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "你是一个专业的学术翻译和总结专家。"},
            # 👇 注意：这里我们只把 title 发给 AI
            {"role": "user", "content": f"请根据这篇论文的英文标题，用中文写一段100字左右的摘要。必须返回严格的 JSON 格式，键名为 'summary'。标题：{title}"}
        ],
        "response_format": {"type": "json_object"}
    }
    
    res = requests.post(url=api_url, headers=headers, json=payload)
    
    if res.status_code == 200:
        ai_text = res.json()["choices"][0]["message"]["content"]
        data = json.loads(ai_text)
        
        # 直接拿到字符串，别用 join！
        summary = data["summary"] 
        print("--- 摘要生成成功 ---")
        print(summary)
        
        # 4. 【核心】用 UPDATE 语句更新到当前 id 对应的行！
        cursor.execute(
            "UPDATE documents SET abstract = ? WHERE id = ?", 
            (summary, doc_id)
        )
        conn.commit()
        print("✅ 已更新回数据库！")
    else:
        print("请求失败：", res.text)

    time.sleep(1)

cursor.execute("SELECT * FROM documents")
results = cursor.fetchall()
print (results)
print("--- 查询所有用户 ---")
for row in results:
    print(row)


conn.close()
print("\n全部处理完成！")
print()