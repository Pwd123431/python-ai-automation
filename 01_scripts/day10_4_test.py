import os,requests,sys,time,bs4

url = 'http://quotes.toscrape.com/'

#先创建quotes.txt文件，如果已经存在就删除
if os.path.exists('./02_data/quotes.txt'):
    os.remove('./02_data/quotes.txt') 

#提前打开文件，用 'w' 模式，避免重复追加
with open('./02_data/quotes.txt', 'w', encoding='utf-8') as f:
    res = requests.get(url)
    bs = bs4.BeautifulSoup(res.text,'html.parser')
    #【新增】先把第一页的数据写进去！
    quote_tags = bs.select('.text')
    author_tags = bs.select('.author')
    for q_tags, a_tags in zip(quote_tags, author_tags):
        f.write(f"【{a_tags.getText()}】说: {q_tags.getText()}\n")

    #找第一页的下一页链接
    next_link = bs.select('.next > a')[0].get('href') if len(bs.select('.next > a')) > 0 else None

    while next_link != None:
        print(f'正在抓取{next_link}页')
        res = requests.get(url + next_link)
        bs = bs4.BeautifulSoup(res.text,'html.parser')
        
        #提取当前页的数据并写入
        quote_tags = bs.select('.text')
        author_tags = bs.select('.author')
        for q_tags, a_tags in zip(quote_tags, author_tags):
            f.write(f"【{a_tags.getText()}】说: {q_tags.getText()}\n")

        print(f'{next_link}页抓取完成')
        #更新下一页链接
        next_link = bs.select('.next > a')[0].get('href') if len(bs.select('.next > a')) > 0 else None
        time.sleep(1)

print("抓取完成！")

