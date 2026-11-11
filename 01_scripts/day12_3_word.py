import docx

#1.加载 Word 文档
doc = docx.Document('./02_data/test.docx')

#2.获取文档的段落数
num_paragraphs = len(doc.paragraphs)
print(f'Word 文档段落数：{num_paragraphs}')

#3.遍历每个段落，提取文本
full_text = ""
for i, paragraph in enumerate(doc.paragraphs):
    text = paragraph.text
    full_text += text + "\n"  # 添加换行符以分隔每段内容
    print(f'第{i + 1}段提取完成')

#4.将提取的文本保存到文件中
with open('./02_data/test_word.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.write(full_text)   

print('提取完成,Word 文本已保存到指定路径：./02_data/test_word.txt')