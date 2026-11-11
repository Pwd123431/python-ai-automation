import openpyxl

#1.加载指定路径的Excel工作簿
wb=openpyxl.load_workbook('./02_data/员工数据.xlsx')
print('文件加载成功，工作簿类型：',type(wb))

#2.获取当前活跃的工作表
sheet=wb['员工数据']
print('读取的表格是：',sheet.title)

#3.获取表格的最大行数和最大列数
max_row=sheet.max_row
max_column=sheet.max_column
print('表格的最大行数：',max_row)
print('表格的最大列数：',max_column)

#4.读取表格中的数据
#读取表头数据
header_list=[]
for col_index in range(1,max_column+1):
    header_list.append(sheet.cell(row=1,column=col_index).value)
print('表头数据：',header_list)

#5.获取指定单元格的数据
name=sheet.cell(row=2,column=1).value
salary=sheet.cell(row=2,column=3).value
print('{}的薪资是：{}'.format(name,salary))


#6.读取表格中的所有数据
print('===========表格中的所有数据如下=========')
for row_index in range(2,max_row+1):
    name=sheet.cell(row=row_index,column=1).value
    department=sheet.cell(row=row_index,column=2).value
    salary=sheet.cell(row=row_index,column=3).value
    print('员工：{},部门：{},薪资：{}'.format(name,department,salary))