import PyPDF2

# 1. 以“读二进制”模式 ('rb') 打开 PDF
# 为什么要用 'rb'？因为 PDF 包含了图片、字体等二进制数据，不是纯文本
with open('./02_data/test.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # 2. 获取 PDF 的页数
    num_pages = len(pdf_reader.pages)
    print(f'PDF 页数：{num_pages}')

    #3.获取第一页的内容
    first_page = pdf_reader.pages[0]

    #第一页纯文本
    text = first_page.extract_text()
    print('--------文本开头--------')
    print(f'第一页内容前300字符：{text[:300]}')