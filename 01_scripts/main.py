from fastapi import FastAPI
import sqlite3

app = FastAPI()

@app.get("/all_docs")
def get_all_documents():
    # 1. 连接数据库
    # ⚠️ 注意路径：因为我们在 01_scripts 里运行，数据库在 02_data 里，所以要退一级
    conn = sqlite3.connect("../02_data/ai_project.db")
    conn.row_factory = sqlite3.Row # 这是一个小魔法，让查出来的数据可以直接转成字典
    
    cursor = conn.cursor()
    
    # 2. 查询所有数据
    cursor.execute("SELECT * FROM documents")
    rows = cursor.fetchall()
    
    # 3. 把数据库里的数据整理成干净的列表
    result = []
    for row in rows:
        result.append({
            "id": row["id"],
            "title": row["title"],
            "keywords": row["keywords"]
        })
        
    conn.close()
    
    # 4. 返回 JSON 数据
    return {
        "status": "success", 
        "count": len(result),
        "data": result
    }