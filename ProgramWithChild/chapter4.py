import urllib
# file = urllib.urlopen('https://www.manning.com/books/hello-world/data/message.txt')
# message = file.read()
# print(message)
import requests
import easygui
url = 'https://www.manning.com/books/hello-world/data/message.txt'
file = requests.get(url)
easygui.msgbox(file.text)
# print(file.text)

# c = 38.8
# print(c)
# print(int(c))
# print(float('76.3'))
# print(type(c))
# print(int(56.78))
# # print(13.2%13)
# # print(13.7%13)
# i = 13.7
# m = i%int(i)
# if m > 0.5:
#     i = int(i) + 1
# else:
#     i = int(i)
# print(i)
# print('请输入你的名字:'),
# name = input()