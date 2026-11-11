import os

# 把拼好的路径存到变量里
path = os.path.join('usr', 'bin', 'spam')

# 打印出来看看
print(path) 
# 1. 看看当前工作目录（你现在在哪个文件夹里干活）
print("当前目录是:", os.getcwd())

# 2. 看看当前目录里有哪些文件（就是你 ls 命令的效果）
print("里面的文件有:", os.listdir('/home/pwt/week1'))

# 3. 拼一个绝对路径
print("绝对路径:", os.path.abspath('day8_1text.py'))

# 4. 文件大小
print("文件大小:", os.path.getsize('.'))  # 返回文件的字节数


#os.makedirs('D:/delicious//walnut//waffles')  # 创建多级目录

print("文件是否存在:", os.path.exists('D:/'))  # 返回布尔值表示文件是否存在

with open('./hello.text') as hellofile:  # 打开一个文件
    helloContent=hellofile.read()  # 读取文件内容
    print(helloContent)  # 打印文件内容
with open('./hello.text') as hellofile:
    lines = hellofile.readlines()
    print(lines)
# 自动关闭，不需要写 close
print("文件是否关闭:", hellofile.closed)

# 写文件（退出 with 缩进后，自动 close）
with open('./bacon.txt', 'w', encoding='utf-8') as f:
    f.write('Hello world!\n')
    f.write('Bacon is not a vegetable.')

# 读文件（退出 with 缩进后，自动 close）
with open('./bacon.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print("==== 文件内容 ====")
    print(content)
with open('./bacon.txt', 'a', encoding='utf-8') as f:  # 追加内容
    f.write('\nBacon is delicious.')
with open('./bacon.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print("==== 文件内容 ====")
    print(content)