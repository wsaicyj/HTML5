import requests
from bs4 import BeautifulSoup

r = requests.get('https://unsplash.com/')
soup = BeautifulSoup(r.text,'lxml')
find = soup.find('div')
print(type(find))
# print(find)
print(find.name)
print(find['id'])
print(find.string)
# print(find)
# print(r.text)