import re

with open('./02_data/墨墨单词.txt', 'r', encoding='utf-8') as f:
    # 按行读取
    lines = f.readlines()

clean_paragraphs = []
for line in lines:
    # 把每一行两头的空白去掉（strip），把中间的多个空格换成一个（re.sub）
    clean_line = re.sub(r' +', ' ', line).strip()
    # 只要不是空行，就加进来
    if clean_line:
        clean_paragraphs.append(clean_line)

# 用两个换行符把段落重新拼接起来
final_text = '\n\n'.join(clean_paragraphs)

with open('./02_data/墨墨单词_paragraphs.txt', 'w', encoding='utf-8') as f:
    f.write(final_text)

print("段落清洗完成！")