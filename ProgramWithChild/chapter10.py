import pygame
import sys
import random

skier_images = ['\\pic\\skier_down.png', '\\pic\\skier_right1.png', '\\pic\\skier_right2.png', '\\pic\\skier_left2.png',
                '\\pic\\skier_left1.png']


class SkierClass(pygame.sprite.Sprite):
    '''创建滑雪者'''

    def __init__(self):
        # 初始化
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('/pic/skier_down.png')
        self.rect = self.image.get_rect()
        self.rect.center = [320, 100]
        self.angle = 0

    def turn(self, direction):
        '''滑雪者转向'''
        self.angle = self.angle + direction
        if self.angle < -2:
            self.angle = -2
        if self.angle > 2:
            self.angle = 2
        center = self.rect.center
        self.image = pygame.image.load(skier_images[self.angle])
        self.rect = self.image.get_rect()
        self.rect.center = center
        speed = [self.angle, 6 - abs(self.angle) * 2]
        return speed

    def move(self, speed):
        '''滑雪者左右移动'''
        self.rect.centerX = self.rect.centerX + speed[0]
        if self.rect.centerX < 20:
            self.rect.centerX = 20
        if self.rect.centerX > 620:
            self.rect.centerX = 620


class ObstacleClass(pygame.sprite.Sprite):
    '''创建树和小旗'''

    def __init__(self, image_file, location, type):
        # 初始化
        pygame.sprite.Sprite.__init__(self)
        self.image_file = image_file
        self.image = pygame.image.load(image_file)
        self.location = location
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.type = type
        self.passed = False

    def scroll(self, t_ptr):
        '''让场景向上滚'''
        self.rect.centerY = self.location[1] - t_ptr

    def create_map(start, end):
        '''创建一个窗口，包含随机的树和小旗'''
        obstacles = pygame.sprite.Group()
        gates = pygame.sprite.Group()
        locations = []
        for i in range(10):
            row = random.randint(start, end)
            col = random.randint(0, 9)
            location = [col * 64 + 20, row * 64 + 20]
            if not (location in locations):
                locations.append(location)
                type = random.choice(['tree', 'flag'])
                if type == 'tree':
                    img = '\\pic\\skier_tree.png'
                elif type == 'flag':
                    img = '\\pic\\skier_flag.png'
                obstacle = ObstacleClass(img, location, type)
                obstacles.add(obstacle)
        return obstacles


    def updateObstacleGroup(map0,map1):
        '''切换到场景的下一屏'''
        obstacles = pygame.sprite.Group()
        for ob in map0:
            obstacles.add(ob)
        for ob in map1:
            obstacles.add(ob)
        return obstacles

    pygame.init()
    screen = pygame.display.set_mode([640,640])
    clock = pygame.time.Clock()
    skier = SkierClass()
    speed = [0,6]
    map_postion = 0
    points = 0
    map0 = create_map(20,29)
    map1 = create_map(10,19)
    activeMap = 0
    obstacles = updateObstacleGroup(map0,map1)
    font = pygame.font.Font(None,50)

    def animate(self):
        '''有移动时重绘屏幕'''
        self.screen.fill([255, 255, 255])
        pygame.display.update(self.obstacles.draw(self.screen))
        self.screen.blit(self.skier.image, self.skier.rect)
        self.screen.blit(self.score_text, [10, 10])
        pygame.display.flip()

    while True:
        clock.tick(30) #每秒更新30次图形
        for event in pygame.event.get():
            #检查按键或窗口是否关闭
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    speed = skier.turn(-1)
                elif event.key == pygame.K_RIGHT:
                    speed = skier.turn(1)
        skier.move(speed) #移动滑雪者
        map_postion += speed[1] #滚动场景

        #从一个场景的窗口切换到另一个场景窗口
        if map_postion >= 640 and activeMap == 0:
            activeMap = 1
            map0 = create_map(20,29)
            obstacles = updateObstacleGroup(map0,map1)
        if map_postion >= 1280 and activeMap == 1:
            activeMap = 0
            for ob in map0:
                ob.location[1] = ob.location[1] - 1280
            map_postion = map_postion - 1280
            map1 = create_map(10,19)
            obstacles = updateObstacleGroup(map0,map1)


        for obstacle in obstacles:
            obstacle.scroll(map_postion)


        #检查是否碰到小树或小旗
        hit = pygame.sprite.spritecollide(skier,obstacles,False)
        if hit:
            if hit[0].type == 'tree' and not hit[0].passed:
                points = points - 100
                skier.image = pygame.image.load('\\pic\\skier_crash.png')
                animate()
                pygame.time.delay(100)
                skier.image = pygame.image.load('\\pic\\skier_down.png')
                skier.angle = 0
                speed = [0,6]
                hit[0].passed = True
            elif hit[0].type == 'flag' and not hit[0].passed:
                points += 10
                obstacles.remove(hit[0])


        #显示得分
        score_text = font.render('Score:' + str(points),1(0,0,0))
        animate()

