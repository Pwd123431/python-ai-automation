num1=float(input("请用户输入一个数字："))
num2=float(input("请用户在输入一个数字："))

add=num1+num2
sub=num1-num2
mul=num1*num2

if(num2==0):
    div="除数不能为0"
else:
    div=num1/num2

# 4. 用 f-string 格式化输出
# f-string（格式化字符串）。它是 Python 里拼接文字和变量最好用、最常用的方法。
#f-string 怎么用？
#很简单，在引号前面加个 f，然后在字符串里面用大括号 {} 把变量包起来。 Python 看到大括号，就会自动把里面的变量替换成对应的值。
print("\n输出结果：\n")
print(f"{num1}+{num2}={add}")
print(f"{num1}-{num2}={sub}")
print(f"{num1}*{num2}={mul}")
print(f"{num1}/{num2}={div}")
