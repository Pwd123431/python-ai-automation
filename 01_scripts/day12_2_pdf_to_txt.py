import PyPDF2

full_text = ""

# 1. 以“读二进制”模式 ('rb') 打开 PDF
with open('./02_data/墨墨单词.pdf', 'rb') as pdf_file:  
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # 2. 获取 PDF 的页数
    num_pages = len(pdf_reader.pages)
    print(f'PDF 页数：{num_pages}')

    # 3. 遍历每一页，提取文本
    for page_num in range(num_pages):
        page = pdf_reader.pages[page_num]
        text = page.extract_text()
        full_text += text + "\n"  # 添加换行符以分隔每页内容
        print('第{}页提取完成'.format(page_num + 1))

# 4. 将提取的文本保存到文件中
with open('./02_data/墨墨单词.txt', 'w', encoding='utf-8') as txt_file:
    txt_file.write(full_text)

print('提取完成,PDF 文本已保存到指定路径：./02_data/墨墨单词.txt')