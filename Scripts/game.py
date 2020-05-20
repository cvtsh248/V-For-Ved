import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *

from sprites import * #dialog, logic

import math

vec = pygame.math.Vector2

pygame.init()
pygame.display.set_caption('V for Ved')

WINDOW_SIZE = (500,500) #subject to change
screen = pygame.display.set_mode(WINDOW_SIZE)

player = Vee()
odd = Odd()
player_group = pygame.sprite.Group(player)
npc_group = pygame.sprite.Group(odd)

p_location = [250,250]
p_yvel = 0

mv_r = False
mv_l = False
jump = False
contact_floor = False

while True: #TO BE TURNED INTO A CLASS
    screen.fill((255,255,255))

    for event in pygame.event.get():
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                mv_r = True
            if event.key == K_LEFT:
                mv_l = True
            if event.key == K_UP:
                jump = True
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                mv_r = False
            if event.key == K_LEFT:
                mv_l = False
            if event.key == K_UP:
                jump = False
    player_group.update(mv_l,mv_r, jump)
    player_group.draw(screen)

    #npc_group.update()
    #npc_group.draw(screen)
 
    pygame.display.update()
    
    clock.tick(10)