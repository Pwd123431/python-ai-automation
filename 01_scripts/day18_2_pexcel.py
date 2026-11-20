import sqlite3
import openpyxl

#建立表格
wb=openpyxl.Workbook()
sheet=wb.active
sheet.title="文献汇总"

# 连接数据库
conn = sqlite3.connect("./02_data/ai_project_v2.db")
cursor = conn.cursor()

# ⚠️ 补上 keywords 列，和你的 Excel 表头对齐
cursor.execute("SELECT id, filename, title, keywords, abstract FROM documents")
rows = cursor.fetchall()
print(f"🎉 数据库里共有 {len(rows)} 篇论文。\n")

# 写表头
sheet['A1']="id"
sheet['B1']="filename"
sheet['C1']="title"
sheet['D1']="keywords"
sheet['E1']="abstract"

# 👇 核心修改：多重拆包！
# 这段代码的意思是：把 enumerate 给的序号叫 excel_row，把数据库的 5 列数据分别叫 db_id, fname, title, kw, abs
for i, (db_id, fname, title, kw, abs_text) in enumerate(rows):
    
    # 👇 核心公式：第 2 行开始，每次加 2（也就是中间空一行）
    current_row = 2 + i * 2 
    
    print(f'正在写入第 {current_row} 行数据...')

    sheet.cell(row=current_row, column=1, value=db_id)
    sheet.cell(row=current_row, column=2, value=fname)
    sheet.cell(row=current_row, column=3, value=title)
    sheet.cell(row=current_row, column=4, value=kw)
    sheet.cell(row=current_row, column=5, value=abs_text)

# 保存文件！千万别忘了这步！
wb.save("./02_data/论文汇总.xlsx")
print("Excel 导出成功！")

conn.close()