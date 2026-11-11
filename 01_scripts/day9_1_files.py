import os
import shutil

# 1. 创建 backup 文件夹
if not os.path.exists('backup'):
    os.mkdir('backup')
    print("备份文件夹已创建！")

# 2. 遍历当前目录
for filename in os.listdir('.'):
    # 如果是文件夹，直接跳过，不浪费时间
    if os.path.isdir(filename):
        continue
    
    # 如果是 .py 文件，直接复制到 backup 文件夹里
    if filename.endswith('.py'):
        shutil.copy(filename, 'backup')
        print(f"成功备份: {filename}")
    else:
        print(f"{filename} 不是 Python 文件，忽略。")

print("\n所有 .py 文件备份完成！")