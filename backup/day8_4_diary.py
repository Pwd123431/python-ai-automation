import os
import datetime,shelve

with shelve.open('diary') as diary_file:

    if 'name'in diary_file:
        print("欢迎回来", diary_file['name'])
    else:
        diary_file['name'] = input("请输入你的名字:")
        print(diary_file["name"],"名字已保存！")

while True:
    print("1.写日记 2.查看日记 3.退出")
    choice = input("请选择操作:")
    if choice == '1':
        date = str(datetime.date.today())
        with open('my_diary.txt', 'a') as diary_file:
            entry = input("请输入今天的日记内容:")
            diary_file.write(date + ": " + entry + "\n")
            print("日记已保存！")
    elif choice == '2':
        if os.path.exists('my_diary.txt'):
            with open('my_diary.txt', 'r') as diary_file:
                print("==== 日记内容 ====")
                print(diary_file.read())
        else:
            print("你还没有写过日记哦，先选 1 写一篇吧！")
    elif choice == '3':
        print("退出程序，再见！")
        break
    else:
        print("无效的选择，请重新输入。")