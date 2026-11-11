#函数

#Hello函数
def greet(name):
    return "Hello,"+name
result=input("请输入姓名：")
print(greet(result))

#超市算价函数
#输入商品单价和数量
def spket(price,count):
    #计算总价
    t=price*count
    #是否打折
    if t>100:
        total=t*0.9
        return(f"打九折，一共是{total:.2f}")
    else :
        total=t
        return(f"不打折，一共是{total:.2f}")

p=float(input("请输入单价:"))
c=int(input("请输入购买数量："))
print(spket(p,c))