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
    # print(a['style'])
    img_str = a['style']
    # print(img_str.index('"'))
    right = img_str.index('(') + 2
    left = img_str.index(')') - 1
    img = img_str[right:left]
    print('相片URL：',img)


class BeautifulPicture():
    def __init__(self):
        self.headers =  {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.108 Safari/537.36'}
        self.web_rul = 'https://unsplash.com'
        self.save_folder = 'D:\\unloadImg'

    def request(self,url):
        re = requests.get(url)
        return re