import random


#sort方法
num=[]
for i in range(10):
    num.append(random.randint(1,100))
print(num)
num.sort()   
print(num)

grid = [['.', '.', '.', '.', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['.', 'O', 'O', 'O', 'O', 'O'], 
        ['O', 'O', 'O', 'O', 'O', '.'], 
        ['O', 'O', 'O', 'O', '.', '.'], 
        ['.', 'O', 'O', '.', '.', '.'], 
        ['.', '.', '.', '.', '.', '.']] 

# 外层循环：控制列 (共 6 列)
for j in range(len(grid[0])):
    # 内层循环：控制行 (共 9 行)
    for i in range(len(grid)):
        # 按照 grid[行][列] 的顺序打印，并且不换行 (end='')
        print(grid[i][j], end='')
    # 打印完一列（也就是新的一行）之后，换行
    print()