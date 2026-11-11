import os

# 把扫地机器人放在当前目录 ('.')
for root, dirs, files in os.walk('.'):
    print("====================================")
    print(f"📍 我现在所在的文件夹是: {root}")
    print(f"📁 这里的子文件夹有: {dirs}")
    print(f"📄 这里的文件有: {files}")