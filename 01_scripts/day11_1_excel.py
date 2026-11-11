import openpyxl

#1.建立一个新的Excel工作簿
wb=openpyxl.Workbook()
print('创建的工作簿类型：',type(wb))

#2.获取当前活跃的工作表
sheet=wb.active
print('当前活跃的工作表类型：',type(sheet))
print('当前表格的名称：',sheet.title)

#3.修改当前工作表的名称
sheet.title='员工数据'
print('修改后的表格名称：',sheet.title)

#4.在当前工作表中添加数据
sheet['A1']='姓名'
sheet['B1']='部门'
sheet['C1']='薪资'
print('A1单元格的值：',sheet['A1'].value)

#5.在当前工作表中添加数据
data_list=[
    ['张三','技术部',40800],
    ['李四','市场部',15000],
    ['王五','人事部',24000]
]
for row_index,row_data in enumerate(data_list,start=2):
    print('正在写入第{}行数据:{}'.format(row_index,row_data))

    #将数据写入工作表
    sheet.cell(row=row_index,column=1,value=row_data[0])
    sheet.cell(row=row_index,column=2,value=row_data[1])
    sheet.cell(row=row_index,column=3,value=row_data[2])

#6.保存工作簿到指定路径
wb.save('./02_data/员工数据.xlsx')
print('工作簿已保存到指定路径：./02_data/员工数据.xlsx')