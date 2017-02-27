import requests
import time
from bs4 import BeautifulSoup
import os

'''
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
'''

class BeautifulPicture:
    def __init__(self):
        self.headers =  {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.108 Safari/537.36'}
        self.web_url = 'https://unsplash.com'
        self.folder_path = 'D:\\unloadImg'

    def request(self,url):
        re = requests.get(url,headers=self.headers)
        return re

    def mkdir(self,path):
        '''创建文件夹'''
        path = path.strip()
        isExists = os.path.exists(path)
        if not isExists:
            print('创建名字叫做%s的文件夹' % path)
            os.makedirs(path)
            print('创建成功')
        else:
            print('%s文件夹已经存在了！')


    def save_img(self,url,name):
        '''保存图片'''
        print('开始保存图片')
        img = self.request(url)
        time.sleep(5)
        file_name = name + '.jpg'
        print('开始保存文件')
        f = open(file_name,'ab')
        f.write(img.content)
        print(file_name,'文件保存成功')
        f.close()

    def get_pic(self):
        print('开始网页请求')
        r = self.request(self.web_url)
        print('开始获取所有a标签')
        all_a = BeautifulSoup(r.text,'lxml').find_all('a',class_='cV68d') #获取网页中的class为cV68d的所有标签
        print('开始创建文件夹')
        self.mkdir(self.folder_path)
        print('开始切换文件夹')
        os.chdir(self.folder_path)
        i = 1 #后面用来命名图片
        for a in all_a:
            img_str = a['style'] #a标签中完整的style字符串
            print('a标签的style内容:%s' % img_str)
            right = img_str.index('(') + 2
            left = img_str.index(')') - 1
            img_url_final = img_str[right:left]
            print('截取后的图片url是:%s' % img_url_final)
            self.save_img(img_url_final,str(i))
            i += 1




# beauty = BeautifulPicture()
# beauty.get_pic()
print(str(1))
