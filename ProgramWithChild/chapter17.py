import pygame
import sys, random


# class MySkier(pygame.sprite.Sprite):
#     def __init__(self, image_file, location,speed):
#         pygame.sprite.Sprite.__init__(self)  # 初始化动画精灵
#         self.image = pygame.image.load(image_file)  # 向其中加载图像文件
#         self.rect = self.image.get_rect()  # 得到定义图像边界的矩形
#         self.rect.left, self.rect.top = location  # 设置滑雪的初始位置
#         self.speed = speed
#
#     def move(self):
#         self.rect = self.rect.move(self.speed)
#         if self.rect.left < 0 or self.rect.right > width: #检查是否碰到窗口左右两边，如果是，让x-speed反向
#             self.speed[0] = -self.speed[0]
#         if self.rect.top < 0 or self.rect.bottom > height: #检查是否碰到窗口上下两边，如果是，让y-speed反向
#             self.speed[1] = -self.speed[1]
#
#
# pygame.init()
# size = width,height = 640,480
# screen = pygame.display.set_mode(size)
# # screen.fill([255,255,255])
# img_file = "skier_crash.png"
# skiers = []
# for row in range(0, 3):
#     for column in range(0, 3):
#         location = [column * 180 + 10, row * 180 + 10]  # 每次循环时都有一个不同的位置
#         speed = [random.choice([-2, 10]), random.choice([-2, 2])]
#         skier = MySkier(img_file, location,speed)
#         skiers.append(skier)
# # for skier in skiers:
# #     print(skier.rect)
# #     screen.blit(skier.image,skier.rect)
# # pygame.display.flip()
#
#
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#     pygame.time.delay(20)
#     screen.fill([255,255,255])
#     for skier in skiers:
#         # print(skier.rect)
#         skier.move()
#         screen.blit(skier.image, skier.rect)
#     pygame.display.flip()
class MySkier(pygame.sprite.Sprite):
    def __init__(self,image_file,location,speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speed[1] = -self.speed[1]



pygame.init()
size = width,height = 640,480
screen = pygame.display.set_mode(size)
screen.fill([255,255,255])
image_file = 'skier_crash.png'
skiers = []
for row in range(0,3):
    for column in range(0,3):
        location = [ column * 180 + 10,row * 180 + 10]
        speed = [random.choice([-2,10]),random.choice([-2,2])]
        skier = MySkier(image_file,location,speed)
        skiers.append(skier)
# for skier in skiers:
#     screen.blit(skier.image,skier.rect)
# pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.time.delay(20)
    screen.fill([255,255,255])
    for skier in skiers:
        skier.move()
        screen.blit(skier.image,skier.rect)
    pygame.display.flip()