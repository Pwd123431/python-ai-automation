import requests,bs4

# 1. 这是一个专门给新手练习爬虫的名言网站，非常安全
url = 'http://quotes.toscrape.com/'

# 2. 发送 GET 请求，把网页“拿”下来
res=requests.get(url)

#3.检查状态码（200表示成功，如果报了别的错发给我）
print('网络状态码：',res.status_code)

#4.打印网页前500个字符
print('网页前500个字符：',res.text[0:500])


#5.把抓回来的 HTML 字符串，丢给 BeautifulSoup 去解析
bs=bs4.BeautifulSoup(res.text,'html.parser')

#6.打印bs数据类型
print('解析后bs数据类型：',type(bs))

#7.找到网页标题
title_tag=bs.select('title')
print('网页标题：',title_tag)

#8.找到网页中所有的名言(class='text')
quote_tags=bs.select('.text')
print('网页中名言数量：',len(quote_tags))

#9.作者数量（class='author'）
author_tags=bs.select('.author')
print('网页中作者数量：',len(author_tags))

#10.打印第一句名言（还记得怎么取列表第一个元素吗？用 [0]）
print('网页中第一句名言：',quote_tags[0].getText())
print('网页中第一句名言作者：',author_tags[0].text)

#11.打印前20句名言
print('\n======网页中所有句名言======：\n')
for q_tags,a_tags in zip(quote_tags,author_tags):
    quote = q_tags.getText()
    author = a_tags.getText()
    print(f"【{author}】说: {quote}")