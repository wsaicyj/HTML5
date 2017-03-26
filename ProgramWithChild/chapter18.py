import pygame,sys

class Skier(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

    def move(self):
        if self.rect.left <= screen.get_rect().left or \
                        self.rect.right >= screen.get_rect().right:
            self.speed[0] = -self.speed[0]
        newpos = self.rect.move(self.speed)
        self.rect = newpos


pygame.init()
delay = 100
interval = 50
pygame.key.set_repeat(delay,interval)    #按键重复事件
pygame.time.set_timer(pygame.USEREVENT,100)  #设置定时器
size = width, height = [640, 480]
screen = pygame.display.set_mode(size)
# screen.fill([255,255,255])
print(screen.get_size())
background = pygame.Surface(screen.get_size())
background.fill([255,255,255])
clock = pygame.time.Clock()
skier = Skier('skier_crash.png', [10, 0], [20, 20])
held_down = False  #判断鼠标按钮是否按下
direction = 1
# print(pygame.NUMEVENTS)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.USEREVENT:
            skier.rect.centery = skier.rect.centery + (30*direction)
            if skier.rect.top <= 0 or \
                skier.rect.bottom >= screen.get_rect().bottom:
                    direction = -direction
        # elif event.type == pygame.KEYDOWN:  #检测键盘按下事件
        #     if event.key == pygame.K_UP:
        #         skier.rect.top -= 10
        #     elif event.key == pygame.K_DOWN:
        #         skier.rect.top += 10
        #     elif event.key == pygame.K_RIGHT:
        #         skier.rect.right += 10
        #     elif event.key == pygame.K_LEFT:
        #         skier.rect.right -= 10
        # elif event.type == pygame.MOUSEBUTTONDOWN:  #检测鼠标按钮是否按下
        #     held_down = True
        # elif event.type == pygame.MOUSEBUTTONUP: #检测鼠标按钮是否弹起
        #     held_down = False
        # elif event.type == pygame.MOUSEMOTION:
        #     if held_down:
        #         skier.rect.center = event.pos  #拖动鼠标时才执行

    clock.tick(30)
    screen.blit(background, (0, 0))
    skier.move()
    screen.blit(skier.image, skier.rect)
    pygame.display.flip()
