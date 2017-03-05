import easygui
import random


num1 = random.randint(1,99)
num2 = random.randint(1,99)

# if num1 > num2:
#     easygui.msgbox('%d比%d大' % (num1,num2))
# if num1 < num2:
#     easygui.msgbox('%d比%d小' % (num1,num2))
# if num1 == num2:
#     easygui.msgbox('%d等于%d大' % (num1,num2))
# if num1 >= 75:
#     easygui.msgbox('最低数为75')
# elif num1 >= 50:
#     easygui.msgbox('最低数为50')
# elif num1 >= 25:
#     easygui.msgbox('最低数为25')
# else:
#     easygui.msgbox('最低数为1')
#习题1
def promotion():
    if  num1 > 50:
        p = num1 - num1 * 0.2
        easygui.msgbox('恭喜你，这件商品原价是%s元,能打8折，打完折后的价格是:%s元' % (num1,p))
    else:
        p = num1 - num1 * 0.1
        easygui.msgbox('恭喜你，这件商品原价是%s元,能打8折，打完折后的价格是:%s元' % (num1,p))

#promotion()


def footballTeam():
    sex = easygui.enterbox('你的性别是:','第一轮筛选')
    if sex == '女':
        age = easygui.integerbox('你的性别是女，恭喜你进入首轮筛选，第二轮筛选是：请问你的年龄是多大?','第二轮筛选')
        if 10 <= age <= 12:
            easygui.ynbox('恭喜你通过第二轮筛选，请问你是否要加入球队?',choices=['加入','不加'])
        else:
            easygui.msgbox('不好意思，你的年龄不符合球队的要求!')
    else:
        easygui.msgbox('不好意思，你的性别不符合球队的要求!')

#footballTeam()


def check():
    pwd = '123456'
