import requests,bs4

url = 'http://quotes.toscrape.com/'

# 发送 GET 请求，把网页“拿”下来
response = requests.get(url)

# 1. 把抓回来的 HTML 字符串，丢给 BeautifulSoup 去解析
soup = bs4.BeautifulSoup(response.text, 'html.parser')

# 2. 找到网页的标题
print("网页的标题是：", soup.title.string) 

# 3. 找到网页中所有的名言
quotes = soup.find_all('span', class_='text')
print("网页中所有的名言：")
for quote in quotes:
    print(quote.string)

