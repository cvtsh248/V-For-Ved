import random
import math
import pygame, sys
import os
from pygame.locals import *

class Dust(pygame.sprite.Sprite):
    def __init__(self, xloc, yloc, screen):
        super(Tile, self).__init__()
        self.path = os.path.dirname(os.getcwd())+'/Assets/effects/DUST.png'
        self.image = pygame.image.load()
        self.location = [xloc,yloc]
        self.rect = self.image.get_rect(center=self.location)
        self.rect.x = self.location[0]
        self.rect.y = self.location[1]
        self.particles = []

