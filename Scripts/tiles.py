import random
import math
import pygame, sys
import os
from pygame.locals import *

class Tile(pygame.sprite.Sprite):
    def __init__(self):
        super(Tile, self).__init__()
        self.location = [250,250]
        self.rect = pygame.Rect(5, 5, 32, 32)
        self.rect.center = (250, 250)