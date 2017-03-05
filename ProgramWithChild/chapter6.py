import easygui
import random


'''
按钮:buttonbox
对话框:msgbox
选择框:choicebox
整数输入框:integerbox
'''
l = ['草莓','巧克力','西瓜']
#flavor = easygui.buttonbox('你喜欢什么口味的冰淇淋?',choices=l)
# flavor = easygui.choicebox('你喜欢什么口味的冰淇淋?',choices=l)
# flavor = easygui.enterbox('你喜欢什么口味的冰淇淋?',default='香蕉')
# flavor = easygui.integerbox('输入的整数是:')
# easygui.msgbox( flavor)
# easygui.fileopenbox()
# easygui.diropenbox()

def guessNumber():
    secret = random.randint(1,99)
    guess = 0
    i = 1
    easygui.msgbox('你6次的机会在1到99之间猜猜数字')
    while guess != secret and i < 7:
        guess = easygui.integerbox('第%d次,你猜的数字是:' % i)
        if guess > secret:
            easygui.msgbox('你猜的数字比较大')
        elif guess < secret:
            easygui.msgbox('你猜的数字比较小')
        i += 1 #用掉一次机会

    if guess == secret:
        easygui.msgbox('恭喜你猜中了,中奖的数字就是%d' % guess)
    else:
        easygui.msgbox('不好意思，你6次都没猜中，其实中奖的数字是%d' % secret)


#习题一
def changeTemperture():
    F = easygui.integerbox('华氏度为:')
    c = 5 / 9 * (F - 32)
    easygui.msgbox('摄氏度为：%f' % c)

#changeTemperture()

def adress():
    msg = '输入收货人信息'
    title = '收货人信息'
    fieldNames = ['姓名','收货地址','邮编','手机号码']
    fieldValues = []
    fieldValues = easygui.multenterbox(msg,title,fieldNames)
    print(fieldValues)

    while 1:
        if fieldValues == None:break
        errmsg = ''
        for i in range(len(fieldNames)):
            # print(i,len(fieldNames))
            if fieldValues[i] == '':
                errmsg = '%s不能为空!' % fieldNames[i]
                fieldValues = easygui.multenterbox(errmsg, title, fieldNames, fieldValues)
        if errmsg == '':break


    easygui.msgbox('收货人信息为:%s' % fieldValues)

    # name = easygui.enterbox('请问你叫什么名字?')
    # province = easygui.enterbox('请问你的具体地址是在哪里？')
    # code = easygui.enterbox('请问邮政编号是多少？')
    # easygui.ynbox('请确认你的收货信息:\n姓名:%s\n地址:%s\n邮政编码:%s' %(name,province,code),choices=['确认','取消'])


adress()
# fieldNames = ['姓名','收货地址','邮编','手机号码']
# for i in range(len(fieldNames)):
#     print(i,fieldNames[i])