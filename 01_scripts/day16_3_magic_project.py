import PyPDF2,sqlite3
import requests,json


#读取pdf
with open("./02_data/test.pdf",'rb') as f:
    reader=PyPDF2.PdfReader(f)

    #读取第一页
    page=reader.pages[0]
    pdf_text=page.extract_text()
print("pdf读取成功，长度：",len(pdf_text))


api_url = "https://api.deepseek.com/chat/completions"
api_key = "sk-c7ffe0af2a9048fcb3930a8e1e622750"

header={
    "Content-Type":"application/json",
    "Authorization":f"Bearer {api_key}"
}

pay_load={
    "model":"deepseek-chat",
    "messages":[
        {"role":"system","content":"你是一个专业的信息提取器。"},
        {"role":"user","content":f"请从以下文本中提取信息，并返回 JSON 格式，必须包含两个键：'title'（标题）和 'keywords'（一个包含3个关键词的列表）。文本内容：{pdf_text}"}
    ],
    "response_format":{"type": "json_object"} # 上封印！
}

print("正在呼叫AI解析PDF...")
res=requests.post(url=api_url,headers=header,json=pay_load)

if res.status_code==200:
    ai_text = res.json()["choices"][0]["message"]["content"]
    data = json.loads(ai_text)
    print("\n--- AI 提取成功 ---")
    print("标题:", data["title"])
    print("关键词:", data["keywords"])

#连接数据库
conn=sqlite3.connect("./02_data/ai_project.db")
cursor=conn.cursor()

# 建表（如果没建过的话）
cursor.execute('''
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        keywords TEXT
    )
''')

# 清空表里的所有旧数据 (但保留表本身的结构)
cursor.execute("DELETE FROM documents")

# 把关键词列表变成字符串存进去
keywords_str = ", ".join(data["keywords"])

# 插入数据！
cursor.execute("INSERT INTO documents (title, keywords) VALUES (?, ?)", (data["title"], keywords_str))
conn.commit()
cursor.execute("SELECT * FROM documents")
results = cursor.fetchall()
print (results)
print("--- 查询所有用户 ---")
for row in results:
    print(row)


conn.close()

print("\n--- 数据已成功存入数据库！---")