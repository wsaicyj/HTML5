#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import pygame
import os,sys



pygame.init()         #初始化pygame
pygame.mixer.init()    #初始化mixer

screen = pygame.display.set_mode([640,480])    #创建一个pygame窗口
background = pygame.Surface(screen.get_size())
background.fill([255,255,255])
pygame.time.delay(2000)     #等待2秒让mixer完成初始化

path = os.getcwd()    #获取当前文件路径
# base_dir = os.path.dirname(os.path.abspath(__file__))
sound_path = os.path.join(path, 'sounds')
# splat_file = "D:\PytharmProject\HTML5\ProgramWithChild\sounds\splat.wav"
# splat_file = sound_path + '\splat.wav'
splat_file = sound_path + r'\bg_music.mp3'

# splat = pygame.mixer.Sound(splat_file)     #创建声音对象
# splat.play()          #播放声音
pygame.mixer.music.load(splat_file)
pygame.mixer.music.play()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()