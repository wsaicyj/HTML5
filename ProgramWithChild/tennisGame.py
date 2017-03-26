#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame,sys,random

# class Tennis(pygame.sprite.Sprite):
#     '''球类定义'''
#     def __init__(self, image_file, speed, location):
#         pygame.sprite.Sprite.__init__(self)
#         self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location
#         self.speed = speed
#
#     def move(self):
#         global points,score_text
#         self.rect = self.rect.move(self.speed)
#         if self.rect.left < 0 or self.rect.right > width:     #球碰到左右两边反弹
#             self.speed[0] = -self.speed[0]
#         if self.rect.top < 0:                                 #球碰到顶边反弹
#             self.speed[1] = -self.speed[1]
#             points += 100
#             score_text = font.render('Score:%s' % str(points), 1, (0, 255, 0))
#
#
#
#
# class Racket(pygame.sprite.Sprite):
#     '''球拍类定义'''
#     def __init__(self, image_file, location):
#         pygame.sprite.Sprite.__init__(self)
#         image_surface = pygame.Surface([100,20])
#         image_surface.fill([0, 0, 0])   #用黑色填充
#         self.image = image_surface.convert() #将表面转换到一个图像
#         # self.image = pygame.image.load(image_file)
#         self.rect = self.image.get_rect()
#         self.rect.left, self.rect.top = location
#
#
#
# pygame.init()
# size = width, height = [640, 480]
# screen = pygame.display.set_mode(size)
# background = pygame.Surface(screen.get_size())
# background.fill([255, 255, 255])
# image_file = 'tennis.jpg'
# racket_image = 'racket.jpg'
# speed = [random.choice([-4, 4]), random.choice([-4, 4])]    #球速度
# location = [300, 10]
# tennis = Tennis(image_file, speed, location)   #创建乒乓球实例
# ballGroup = pygame.sprite.Group(tennis)
# racket = Racket(racket_image, [320, 400])  #创建球拍实例
# clock = pygame.time.Clock()  #设置计时
# held_down = False   #判断鼠标按钮是否有按下
# done = False
# points = 0
# lives = 3     #生命数
# font = pygame.font.Font(None, 50)   #创建字体对象
# score_text = font.render('Score:%s' % str(points), 1, (0, 255, 0))  #渲染文本:得分
# score_pos = [10, 10]
# lives_pos = [300,10]
#
# while 1:
#     clock.tick(90)
#     screen.blit(background, [0, 0])
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             held_down = True
#         elif event.type == pygame.MOUSEBUTTONUP:
#             held_down = False
#         elif event.type == pygame.MOUSEMOTION:
#             if held_down:
#                 racket.rect.centerx = event.pos[0]     #如果鼠标移动，球拍就横着移动
#
#     if pygame.sprite.spritecollide(racket,ballGroup,False):    #检查球是否碰到球拍
#         tennis.speed[1] = -tennis.speed[1]
#
#     tennis.move()
#
#     if not done:
#         screen.blit(tennis.image, tennis.rect)
#         screen.blit(racket.image, racket.rect)
#         screen.blit(score_text, score_pos)
#         for i in range(lives):
#             width = screen.get_width()
#             screen.blit(tennis.image, [width - 40 * i, 10])
#         pygame.display.flip()
#
#     if tennis.rect.top >= screen.get_rect().bottom:
#         lives -= 1
#         if lives == 0:
#             final_text1 = 'Game Over'
#             final_text2 = 'Your final score is:%s' % str(points)
#             ft1_font = pygame.font.Font(None,70)
#             ft1_surf = font.render(final_text1, 1, (255, 0, 0))
#             ft2_font = pygame.font.Font(None, 50)
#             ft2_surf = font.render(final_text2, 1, (0, 0, 255))
#             screen.blit(ft1_surf, [screen.get_width()/2 - ft1_surf.get_width()/2, 150])
#             screen.blit(ft2_surf, [screen.get_width()/2 - ft2_surf.get_width()/2, 250])
#             pygame.display.flip()
#             done = True
#         else:
#             pygame.time.delay(2000)
#             tennis.rect.topleft = [50, 50]

class Tennis(pygame.sprite.Sprite):
    '''创建乒乓球类'''
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)      #初始化Sprite
        self.image = pygame.image.load(image_file)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def move(self):    #重写move方法
        global score, score_text
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > width:  #碰到左右两边反转
            self.speed[0] = -self.speed[0]

        if self.rect.top < 0:     #碰到上方反转
            score += 100
            score_text = font.render('Score:%s' % score, 1, [0, 255, 0])
            self.speed[1] = -self.speed[1]


class Racket(pygame.sprite.Sprite):
    '''创建球拍类'''
    def __init__(self, location):
        pygame.sprite.Sprite.__init__(self)   #初始化Sprite
        racket = pygame.Surface([100,20])
        racket.fill([0, 0, 0])
        self.image = racket.convert()
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location



pygame.init()
size = width, height = [640, 480]
screen = pygame.display.set_mode(size)
background = pygame.Surface(screen.get_size())
background.fill([255, 255, 255])
tennis_image = 'tennis.jpg'
tennis_speed = [random.choice([-4, 4]), random.choice([-4, 4])]
tennis_location = [320, 50]
tennis = Tennis(tennis_image, tennis_speed, tennis_location)  #创建tennis实例
tennis_group = pygame.sprite.Group()     #创建组
tennis_group.add(tennis)
racket_location = [280, 400]
racket = Racket(racket_location)   #创建Racket实例
clock = pygame.time.Clock()        #设置定时器
font = pygame.font.Font(None,50)    #创建字体
score = 0    #得分
score_location = [10,10]    #得分显示位置
score_text = font.render('Score:%s' % score, 1, [0, 255, 0])
lives = 3    #生命数
lives_location = [320,10]     #生命数显示位置
# lives_text = font.render('Score:%s' % lives, 1, [255, 0, 0])
done = False



while 1:
    clock.tick(30)
    screen.blit(background, [0, 0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            racket.rect.centerx = event.pos[0]

    if pygame.sprite.spritecollide(racket, tennis_group, False):     #检测球是否碰撞到球拍
        tennis.speed[1] = -tennis.speed[1]

    tennis.move()

    if not done:
        screen.blit(score_text, score_location)
        screen.blit(tennis.image, tennis.rect)
        screen.blit(racket.image, racket.rect)
        for i in range(lives):
            width = screen.get_width() - 100
            screen.blit(tennis.image, [width - 40 * i, 10])
        pygame.display.flip()

    if tennis.rect.top >= screen.get_rect().bottom:  #如果球碰到底边就减一条命
        lives -= 1
        if lives == 0:
            final_text1 = 'Game Over'
            final_text2 = 'Your final score is: %s' % str(score)
            ft1_surf = font.render(final_text1, 1, [255, 0, 0])
            ft2_surf = font.render(final_text2, 1, [0, 0, 255])
            screen.blit(ft1_surf, [screen.get_width()/2 - ft1_surf.get_width()/2, 150])
            screen.blit(ft2_surf, [screen.get_width()/2 - ft2_surf.get_width()/2, 250])
            pygame.display.flip()
            done = True
        else:
            pygame.time.delay(2000)
            tennis.rect.topleft = [50, 50]


