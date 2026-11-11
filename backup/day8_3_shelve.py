import shelve

# 重新打开存档
with shelve.open('game_save') as save_file:
    # 像查字典一样取出来
    print("读取玩家名字:", save_file['name'])
    print("读取玩家等级:", save_file['level'])
    print("读取玩家背包:", save_file['bag'])