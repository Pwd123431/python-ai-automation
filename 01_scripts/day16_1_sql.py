import sqlite3

# 1. 连接到数据库（如果没有这个文件，它会自动创建）
conn=sqlite3.connect("./02_data/test.db")

# 2. 创建一个游标（相当于拿笔的手）
cusor=conn.cursor()

#3.创建一张表（如果不纯在的话）
cusor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')
# 清空表里的所有旧数据 (但保留表本身的结构)
cusor.execute("DELETE FROM users")

#4.插入数据
cusor.execute("INSERT into users(name,age) VALUES('张三',23)")
cusor.execute("INSERT into users(name,age) VALUES('李四',22)")

#5.提交数据
conn.commit()

#6.查询数据
cusor.execute("SELECT * FROM users")
results = cusor.fetchall()
print (results)
print("--- 查询所有用户 ---")
for row in results:
    print(row)

cusor.execute("SELECT * FROM users WHERE name='张三'")
stu1=cusor.fetchone()
print(f"张三同学的年龄是{stu1[2]}岁")

cusor.execute("SELECT * FROM users WHERE age==22")
stu2 = cusor.fetchone()
print("年龄22的学生：",stu2[1])  

# 7. 关闭连接
conn.close()