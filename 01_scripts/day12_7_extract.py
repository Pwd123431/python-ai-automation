import re

# 1. 读取你那个充满纯文本的 html 文件
with open('./02_data/word.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 2. 把多行文本压成一行，方便正则匹配
# 把换行符全部替换成空格
flat_text = text.replace('\n', ' ')

# 3. 写出正则表达式
# 分析你的格式：数字(359) + 空格 + 英文单词(specific) + 音标[...] + 后面的解释
# \d+ 匹配数字，\s+ 匹配空格，[a-zA-Z]+ 匹配英文单词，\[.*?\] 匹配中括号里的音标，.*? 匹配后面的解释
pattern = re.compile(r'(\d+)\s+([a-zA-Z]+)\s*\[(.*?)\]\s*(.*?)(?=\s+\d+\s+[a-zA-Z]+|$)')

# 4. 找到所有匹配的单词
matches = pattern.findall(flat_text)

# 5. 清洗并保存
with open('./02_data/words_clean.txt', 'w', encoding='utf-8') as out_file:
    count = 0
    for match in matches:
        word_id = match[0]    # 编号 359
        word = match[1]       # 单词 specific
        phonetic = match[2]   # 音标 sp e' sɪfɪk 
        meaning = match[3]    # 解释 adj. 具体的; 明确的; 特定的 n. 特效药
        
        # 把结果拼成好看的格式，写入文件
        line = f"{word_id}. {word} [{phonetic}] {meaning}"
        out_file.write(line + '\n')
        count += 1

print(f"提取成功！共提取了 {count} 条词条。")