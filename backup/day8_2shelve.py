import shelve

# 1. 打开一个名叫 'game_save' 的存档文件
with shelve.open('game_save') as save_file:
    # 2. 把各种变量存进去（就像给字典赋值一样）
    player_name = "勇者小P"
    player_level = 99
    inventory = ["圣剑", "血瓶", "魔法书"]
    
    save_file['name'] = player_name
    save_file['level'] = player_level
    save_file['bag'] = inventory
    
    print("游戏进度已保存！")