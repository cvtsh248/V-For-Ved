import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *

from sprites import * #dialog, logic

import math

from tiles import *

from lvl import *

from pygame.freetype import *

vec = pygame.math.Vector2

pygame.init()
pygame.display.set_caption('V for Ved')

WINDOW_SIZE = (1280,768) #subject to change
screen = pygame.display.set_mode(WINDOW_SIZE)
tile_group = pygame.sprite.Group()

render = pygame.Surface((1280, 768)) #x value can be changed depending on the level

player = Vee()
odd = Odd()

def loadLevel(X, Y):
    for y in range(0,Y): #render tiles based on tile map
        for x in range(0,X):
            coord = level[y][x]
            if coord == 1:
                tile_group.add(Tile(x*64,y*64,'Assets/Tiles/Mossy_Stone/MOSSY_STONE0.png',1,1))
            if coord == 2:
                tile_group.add(Tile(x*64,y*64,'Assets/Tiles/Mossy_Stone/MOSSY_STONE1.png',1,1))
            if coord == 3:
                tile_group.add(Tile(x*64,y*64,'Assets/Tiles/Mossy_Stone/MOSSY_STONETOP.png',1,1))

GAME_FONT = Font('Fonts/manaspace/manaspc.ttf', 24)

player_group = pygame.sprite.Group(player)
npc_group = pygame.sprite.Group(odd)

p_location = [250,250]
p_yvel = 0

mv_r = False
mv_l = False
jump = False
contact_floor = False

loadLevel(20,12)

camloc = [0,0]

camx = 0

camy = 0

while True: #gameloop
    screen.fill((24,123,120))
    render.fill((24,123,120))

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
    
    if player.mv == 'r':
        camx = -3.8
    elif player.mv == 'l':
        camx = 3.8
    elif player.mv == 'c':
        camx *= 0.9
        #camx = 0
    else:
        camx *= 0.9
        #camx = 0
    camy = (player.yvel/10)
    #camx *= 0.8
    
    camloc[0] += camx
    camloc[1] += camy

    tile_group.draw(render)


    player_group.update(mv_l,mv_r, jump)
    player_group.draw(render)
    screen.blit(render, (camloc[0]-3, camloc[1]+50))


    text_surface, rect = GAME_FONT.render("Hello, VEE!", (0, 0, 0))
    screen.blit(text_surface, (140+camloc[0]*2, 250+camloc[1]*2))

    #npc_group.update()
    #npc_group.draw(screen)
    
 
    pygame.display.update()
    
    clock.tick(10)