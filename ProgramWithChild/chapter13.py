# def calculaterTax(price,tax_rate):
#     total = price + (price * tax_rate)
#     my_price = 10000
#     print('my_price(inside function=)',my_price)
#     return total
#
# my_price = 100
# totalPrice = calculaterTax(my_price,0.06)
# print('price=',my_price,'TotalPrice=',totalPrice)
# print('my_price(outside function=)',my_price)
# def printName(name):
# class Ball:
#     def __init__(self,color,size,direction):
#         self.color = color
#         self.size = size
#         self.direction = direction
#
#     def __str__(self):
#         print('hi,i am a %s %s %s' % (self.size,self.color,self.direction))
#
#     def bounce(self):
#         if self.direction == "down":
#             self.direction = "up"
#
# myBall = Ball("red","small","down")
# print('I just created a ball.')
# print('My ball is',myBall.size)
# print('My ball is',myBall.color)
# print('My ball is direction is',myBall.direction)
# print('Now I am going to bounce the ball')
# print()
# myBall.bounce()
# print('Now the ball is direction is',myBall.direction)
# print(myBall)
# class HotDog:
#     def __init__(self):
#         self.cooked_level = 0  #0-3表示生的；>3表示半生不熟;>5表示已经烤好;>8表示烤成木炭
#         self.cooked_string = 'Raw' #描述热狗的生熟程度
#         self.condiments = [] #配料列表
#
#     def cook(self,time):
#         self.cooked_level += time
#         if self.cooked_level > 8:
#             self.cooked_string = "热狗已烤成木炭"
#         elif self.cooked_level > 5:
#             self.cooked_string = '热狗已经烤好'
#         elif self.cooked_level > 3:
#             self.cooked_string = '热狗处于半生不熟状态'
#         else:
#             self.cooked_string = '热狗还是生的'
#
#     def add_condiment(self,condiment):
#         self.condiments.append(condiment)
#
#
# myHotDog = HotDog()
# myHotDog.cook(9)
# print(myHotDog.cooked_level)
# print(myHotDog.cooked_string)
# print(myHotDog.condiments)
class GameObject:
    def __init__(self,name):
        self.name = name

    def pickUp(self,player):
        pass

class Coin(GameObject):
    def __init__(self,value):
        GameObject.__init__(self)
        self.value = value

    def spend(self,buyer,seller):
        pass