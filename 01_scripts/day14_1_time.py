import time,datetime

#1.获取时间戳，从1970年算起的秒数
timetampt=time.time()
print('当前时间戳为：',timetampt)

#2.获取当前时间
nowtime=datetime.datetime.now()
print('当前时间为：',nowtime)

# 3. 格式化输出时间（把时间变成你想要的字符串样子）
# %Y是年，%m是月，%d是日，%H是时，%M是分，%S是秒
formatted_time=nowtime.strftime("%Y年%m月%d日 %H:%M:%S")
print("格式化后的时间:", formatted_time)

print('======模拟大模型思考时间======')
start_time=time.time()#开始时间

print("正在呼叫大模型...")
time.sleep(2) # 程序暂停 2 秒（模拟网络延迟）

end_time=time.time()#结束时间
cost_time=round(end_time-start_time,2)#程序思考的时间
print(f"大模型回答完毕！耗时 {cost_time} 秒。")


import subprocess

# 在 Ubuntu 下，用代码启动系统的计算器
# 注意：如果你没有安装计算器可能报错，这只是一种思路
#print("\n正在尝试打开计算器...")
#subprocess.Popen(['gnome-calculator']) 
# 我们用个更通用的，用默认浏览器打开一个网址
import webbrowser
webbrowser.open("https://www.baidu.com")
print("已经用代码帮你打开了浏览器！")
