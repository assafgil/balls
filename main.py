import pygame
import time

import array
from array import *

width, height = 1000, 1000
dx, dy = 0,0
mx, my = 0,0
x,y = 100, 0
c1 = (0,0,255)
c2 =(0,0,0)



pygame.init()

red = (255, 0, 0)
font = pygame.font.SysFont('segoeui', 40)
passed_screen = False

rect_width,rect_height = 20,20
#qx, qy = 6,6
#up = True
screen = display = pygame.display.set_mode((width, height))
screen.fill((0,0,0))
sp = pygame.image.load('basketball.png').convert_alpha()
sp = pygame.transform.scale(sp, (rect_width,rect_height))
sp_rect = sp.get_rect()
sp_rect= sp_rect.move(rect_width*14,rect_height*23)
last_dir = 0
move_size: int = 2 #1,2,4,5,10,20
game_loop = True
while game_loop:
    display.fill((255, 255, 0))
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        game_loop = False



    if passed_screen:

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                my = -move_size
            elif event.key == pygame.K_DOWN:
                my = move_size
            elif event.key == pygame.K_LEFT:
                mx = -move_size
            elif event.key == pygame.K_RIGHT:
                mx = move_size

        dx = mx
        dy = my
        if ((sp_rect.right + dx > width) or (sp_rect.left+dx < 0)):
            dx=0
        if ((sp_rect.top + dy < 0 ) or (sp_rect.bottom+dy > height)):
            dy=0



        sp_rect = sp_rect.move(dx, dy)

        display.blit(sp, sp_rect)


        pygame.display.flip()
        pygame.time.wait(1)

    else:
        display.fill((255, 255,0))
        font1 = pygame.font.SysFont('consolas', 17, bold=True)
        text_1 = font1.render('Welcome to my game! Instructions below:', True, (0, 0, 0))
        text_2 = font1.render('Your goal is to reach the basket. Every time you score, you advance to the next level. Each three times you reach the basket, you get more health points.', True, (0, 0, 0))
        text_3 = font1.render('When you get to 0 hp, you lose. When you get to level 10, you win. Move with the arrow keys, and avoid getting blocked. Press any ket to begin.Good luck!', True, (0, 0, 0))
        display.blit(text_1, ((width - text_1.get_width()) // 2, (height - text_1.get_height()) // 2))
        display.blit(text_2, ((width - text_2.get_width()) // 2, (height + 40 - text_2.get_height()) // 2))
        display.blit(text_3, ((width - text_3.get_width()) // 2, (height + 80 - text_3.get_height()) // 2))
        if event.type == pygame.KEYDOWN:
            passed_screen = True
        pygame.display.flip()