import os,zipfile

with zipfile.ZipFile('backup.zip', 'w') as zipf:
    for filename in os.listdir('backup'):
        zipf.write(os.path.join('backup', filename), filename)
        print(f"正在打包: {filename}")
print("\n所有文件已打包完成,生成 backup.zip 文件！")