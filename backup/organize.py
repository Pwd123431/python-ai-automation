import os, shutil

folders = {
    '01_scripts': ['.py'],             # 所有 Python 代码
    '02_data': ['.txt'],               # 所有文本数据
    '03_archives': ['.zip'],           # 压缩包
    '04_saves': ['diary', 'game_save'] # shelve 生成的存档文件
}

for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)

for filename in os.listdir('.'):
    if os.path.isdir(filename) or filename in ['notes.md', 'organize.py']:
        continue

    # 4. 根据后缀或者名字，把文件移动到对应的文件夹里
    moved = False

    for folder, extensions in folders.items():
        for ext in extensions:
            if filename.endswith(ext):
                shutil.move(filename, folder)
                print(f"✅ 已移动 {filename} -> {folder}/")
                moved = True
                break
        if moved:
            break

    if not moved and filename in folders['04_saves']:
        shutil.move(filename, '04_saves')
        print(f"✅ 已移动 {filename} -> 04_saves/")

print("\n🎉 文件整理完毕！")