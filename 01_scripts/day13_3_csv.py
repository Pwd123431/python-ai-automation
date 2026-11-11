import csv

# 准备要写入的数据（这是一个二维列表，每个小列表代表一行）
data = [
    ["姓名", "部门", "薪资"],
    ["张三", "技术部", 40800],
    ["李四", "市场部", 15000],
    ["王五", "人事部", 24000]
]

# 用 'w' 模式打开文件，注意一定要加 newline='',忘记加newline='',将会有两行行距
with open('./02_data/employees.csv', 'w', newline='', encoding='utf-8') as f:
    # 创建 writer 对象
    writer = csv.writer(f)
    
    # 用 writerows() 一次性写入多行
    writer.writerows(data)

print("CSV 文件写入成功！")


#读取csv数据

with open('./02_data/employees.csv','r',encoding='utf-8') as f:
    #创建reader对象
    reader=csv.reader(f)
    for row in reader:
        print(f"当前是第{reader.line_num}行")
        if row[0]!='姓名':
            name=row[0]
            department=row[1]
            salary=row[2]
            print(f"{name}属于{department}薪资是{salary}")
        else :
            print(f"表头为：{row[0]}||{row[1]}||{row[2]}")
    # 读取csv数据（升级版：字典形式）
print("\n--- 升级版字典读取 ---")
with open('./02_data/employees.csv', 'r', encoding='utf-8') as f:
    # 换成 DictReader
    dict_reader = csv.DictReader(f)
    
    for row_dict in dict_reader:
        # 现在的 row_dict 直接就是字典：{'姓名': '张三', '部门': '技术部', '薪资': '40800'}
        print(f"{row_dict['姓名']}属于{row_dict['部门']}薪资是{row_dict['薪资']}")