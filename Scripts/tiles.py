import random
import math
import pygame, sys
import os
from pygame.locals import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, tile_path, tag, map):
        super(Tile, self).__init__()
        self.path = os.path.dirname(os.getcwd())+'/'+tile_path
        self.image = pygame.image.load(self.path)
        self.location = [xloc,yloc]
        self.rect = self.image.get_rect(center=self.location)
        self.rect.x = self.location[0]
        self.rect.y = self.location[1]
        self.image=pygame.transform.scale(self.image,(64,64)) #upscale

