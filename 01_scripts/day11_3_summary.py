import openpyxl

# 1.Load the workbook
wb = openpyxl.load_workbook('./02_data/员工数据.xlsx')
sheet = wb['员工数据']

# 2.计算薪资总和
total_salary = 0
for row_index in range(2, sheet.max_row + 1):
    salary = sheet.cell(row=row_index, column=3).value
    total_salary += salary

print('薪资总和：', total_salary)

#3.另存为新的Excel文件
summary_wb = openpyxl.Workbook()
summary_sheet = summary_wb.active
summary_sheet.title = '薪资汇总'
summary_sheet['A1'] = '报表项目'
summary_sheet['B1'] = '数值'
summary_sheet['A2'] = '公司总薪资'
summary_sheet['B2'] = total_salary

#4.保存新的Excel文件
summary_wb.save('./02_data/薪资汇总.xlsx')
print('薪资汇总已保存到指定路径：./02_data/薪资汇总.xlsx')