


# mycat={'size':'fat','color':"blue",'name':'Jem'}
# print( 'My cat has ' + mycat['color'] + ' fur.')
# print(mycat['name'])

#字典的创建
phone_book={
    'zhangsan':'13800001111',
    'lisi':'13400111100',
    'wangwu':'13711110000'
}
print("zhangsan的电话:",phone_book['zhangsan'])
print("zhaoliu的电话：",phone_book.get('zhaoliu','抱歉，查无此人'))

while True:
    name__=input("请输入你要查询的名字（按q退出）")
    if name__=="q":
        print("退出成功！")
        break

    if name__ in phone_book.keys():
            print(name__,"的电话是",phone_book[name__])
    else:
        print("查无此人,是否添加联系人:y/n")
        t=input()
        if t=='y':
             phone=input("请输入电话号码：")
             phone_book[name__]=phone
             print("添加成功!")
        elif t=='n':
             print("已跳过，继续查询下一个。")
        
