
def displayInventory(spam):
    total=0
    for k,v in spam.items():
        total=total+v
        print(k,v)
    print("Total number of items:",total)
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


displayInventory(stuff)

# 任务1：把句子拆成单词列表
sentence = "I love AI"
word_list = sentence.split() #split() 就像一把刀，默认按空格把句子切成了列表
print("拆开后的列表:", word_list)  # 输出: ['I', 'love', 'AI']

# 任务2：把列表拼成用横杠连接的字符串
joined_text = "-".join(word_list) #join() 就像胶水，把列表里的单词用 - 粘了起来
print("拼起来的句子:", joined_text)  # 输出: I-love-AI

sentence1="I hate the world!"
word=sentence1.split()
print("拆开后的列表：",word)

text="*".join(word)
print("拼起来的句子：",text)