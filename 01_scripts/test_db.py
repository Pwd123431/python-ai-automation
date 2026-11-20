import sqlite3

# 注意：这取决于你从哪个文件夹运行。如果在 01_scripts 下运行，路径就是 ../02_data/ai_project.db
conn = sqlite3.connect("./02_data/ai_project.db")
cursor = conn.cursor()

# 查一下里面还有没有数据
cursor.execute("SELECT id, title, abstract FROM documents")
rows = cursor.fetchall()

print(f"数据库里共有 {len(rows)} 条数据。")
for row in rows:
    print(row)

conn.close()