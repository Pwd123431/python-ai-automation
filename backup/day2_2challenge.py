#温度转换

#输入摄氏度
C=float(input("请输入摄氏度："))
#转化为华氏度
F = C * 9/5 + 32
#输出
print(f"摄氏度{C}=华氏度{F:.2f}")

#计算圆的面积
23
#输入半径
r=float(input("请输入圆的半径："))
#计算面积
a=3.14159*r*r
#输出结果
print(f"圆的面积={a:.2f}")

#超市结账

#输入商品单价和数量
d=float(input("请输入商品单价："))
s=float(input("请输入购买数量："))
#计算总价
t=d*s
#是否打折
if t>100:
    total=t*0.9
    print(f"打九折，一共是{total:.2f}")
else :
    total=t
    print(f"不打折，一共是{total:.2f}")

