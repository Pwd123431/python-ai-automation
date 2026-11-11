import requests

# 1. 这是一个专门给新手练习爬虫的名言网站，非常安全
url = 'http://quotes.toscrape.com/'

# 2. 发送 GET 请求，把网页“拿”下来
response = requests.get(url)

# 3. 检查状态码（200表示成功，如果报了别的错发给我）
print("网络状态码:", response.status_code)

# 4. 网页的源代码（HTML）就存在 response.text 里
print("网页的标题是：")
# 咱们随便截取网页源代码的前 200 个字符看看
print(response.text[:200]) 