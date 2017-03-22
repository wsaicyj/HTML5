import pygame
import sys,random
# from pygame.color import THECOLORS
from pygame.color import THECOLORS
import math


'''
# r = random.choice(THECOLORS.keys())
x = [x for x in THECOLORS.keys()]
print(x)
# print(r)
'''
pygame.init()
screen = pygame.display.set_mode([640,480])
screen.fill([255,255,255])
# pygame.draw.circle(screen,[255,0,0],[100,100],30,2)
# pygame.draw.rect(screen,[0,255,0],[250,150,300,200],2)
# pygame.display.flip()
# for i in range(100):
#     width = random.randint(0,250)
#     height = random.randint(0,100)
#     top = random.randint(0,400)
#     left = random.randint(0,500)
#     color_list = [x for x in THECOLORS.keys()] #列表推导式
#     color_name = random.choice(color_list)
#     color = THECOLORS[color_name]
#     line_width = random.randint(1,3)
#     pygame.draw.rect(screen,color,[left,top,width,height],line_width)
# plotPoints = []
# for x in range(0,640):
#     y = int(math.sin(x/640.0 * 4 * math.pi) * 200 + 240)
#     plotPoints.append([x,y])
# pygame.draw.lines(screen,[0,0,0],False,plotPoints,3)
# pygame.draw.rect(screen,[0,0,0],[x,y,1,1],1)
my_skier = pygame.image.load("skier_crash.png")
x = 50
y = 50
speed = 10
screen.blit(my_skier,[x,y])
pygame.display.flip()
# for i in range(1,10):
#     pygame.time.delay(2000)
#     pygame.draw.rect(screen,[255,255,255],[x,50,70,70])
#     x += 100
#     screen.blit(my_skier,[x,50])
#     pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.time.delay(20)
    pygame.draw.rect(screen,[255,255,255],[x,y,90,90])
    if x > screen.get_width() - 90 or x < 0:
        pass