
#while循环

while True:
    print ("请输入一个数字：")
    number=int(input())
    if number==0:
        print("退出成功！")
        break

#for循环
for i in range(5,11):
    print(i)

print("\n--- 考试成绩判断 ---")
scores = [85, 92, 78, 60, 45]

t=0
for s in scores:
    if s >= 60:
        print(f"{s} 分及格了")
    else:
        print(f"{s} 分挂科了")
    t=t+1
print(f"for循环循环了{t} 次")