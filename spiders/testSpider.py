import requests
from bs4 import BeautifulSoup

#给请求指定一个请求头来模拟chrome浏览器
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.108 Safari/537.36'}
web_url = 'https://unsplash.com'
r = requests.get(web_url,headers=headers)
# print(r.text)
all_a = BeautifulSoup(r.text,'lxml').find_all('a',class_='cV68d')
# print(all_a)
for a in all_a:
    print(a['style'])