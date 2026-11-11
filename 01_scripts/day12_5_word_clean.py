import re

# 这是模拟用 PyPDF2 提取出来的乱码文本（双栏挤在一起）
dirty_text = """
1 guy [gai]n. 家伙; 人22 [fɔːt]n. 故障; 过错; 缺陷; 断层
v. 发现错误; 找出缺点2 found [fɔːnd]v. 建立; 创建
v. 找到; 发现; 认为; “find”的过去式和过去分词23 [terrible] [terb(ə)l]adj. 可怕的
"""

# 1. 先把所有的换行符替换成空格，把文本连成一长串
flat_text = dirty_text.replace('\n', ' ')

# 2. 核心正则：(单词) + [音标] + (中文释义)
# \b[a-zA-Z]+\b 匹配纯英文单词
# \[.*?\] 匹配中括号里的音标
# .*?(?=\b[a-zA-Z]+\b|$) 匹配从音标后一直到下一个英文单词之前的所有内容（也就是释义）
pattern = re.compile(r'(\b[a-zA-Z]+\b)\s*\[(.*?)\]\s*(.*?)(?=\b[a-zA-Z]+\b\s*\[|$)')

# 3. 提取所有匹配项
matches = pattern.findall(flat_text)

# 4. 清洗结果并保存
cleaned_words = []
for match in matches:
    word = match[0]
    phonetic = match[1]
    meaning = match[2].strip() # 去掉首尾空格
    
    # 过滤掉空释义或者不完整的抓取
    if meaning:
        # 格式化输出：单词 [音标] 释义
        clean_line = f"{word} [{phonetic}] {meaning}"
        cleaned_words.append(clean_line)

# 5. 保存为 txt
with open('./02_data/clean_words.txt', 'w', encoding='utf-8') as f:
    for line in cleaned_words:
        f.write(line + '\n')

print(f"清洗完成！共提取了 {len(cleaned_words)} 个单词。")