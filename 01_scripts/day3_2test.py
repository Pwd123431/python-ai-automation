def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = number * 3 + 1
    
    print(result)  # 书上要求函数里打印
    return result  # 返回结果给外面

# 主程序
try:
    i = int(input("请输入一个整数："))
    while i != 1:
        i = collatz(i)  # 每次把返回的结果重新赋给 i
except ValueError:
    print("请输入有效的整数！")