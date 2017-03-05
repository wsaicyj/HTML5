import easygui
import time


def a():
    someInput = easygui.integerbox('请输入数字:')
    while someInput == 3:
        someInput = easygui.integerbox('还不错哟，输入的都是3')
    easygui.msgbox('你输入的不是3，讨厌')

def b():
    for i in range(1,6):
        easygui.msgbox('i=%d' % i)
        if i == 3:
            continue
        easygui.msgbox('Are you today?')

b()