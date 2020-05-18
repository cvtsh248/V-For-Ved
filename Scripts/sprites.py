import random
import math
import pygame, sys
from pygame.locals import *

#Every important character will have its own class for logic stuff.
class vee(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(self)
        self.images_walk = []
        for i in range (0,20):
            self.images_walk.append(pygame.image.load('<IMGHERE>'+str(i)))
        self.images_idle = []
        for i in range (0,20):
            self.images_idle.append(pygame.image.load('<IMGHERE>'+str(i)))
        #Image and animation stuff to be added

        self.index = 0 #for sprite animations
        self.location = [250,250]

        self.rect = pygame.Rect(5, 5, 32, 32)
        self.rect.center = (250, 250)

        self.health = 100
        self.random_phrases = ['Inilaute Amma', 'By meaning?'] #Random mutterings
        self.phrases_spoken = ['Sexy ass, <name> ah','Shut up', 'Shut up, <name>', 'EEEH', 
                                'ITS YOUR FAULT!', 'EEEEH', 'Eh, you ah!', 'YOU DID IT!', 'Do you want to be belted, <name>?'] #directed at people
    def updatePosition(self,l, r):
        last = ''
        if l == True:
            last = 'l'
            self.location[0]+=1
            self.index += 1
            if self.index >= len(self.images_walk)-1: #walk cycles
                self.index = 0
            self.image=self.images_walk[self.index]
        if r == True:
            last = 'r'
            self.location[0]-=1
            self.index += 1
            if self.index >= len(self.walk)-1: #walk cycle
                self.index = 0
            self.image=self.images_walk[self.index]
        if r == False and l == False:
            self.index += 1
            if self.index >= len(self.images_idle)-1: #idle cycle
                self.index = 0
            self.image=self.images_idle[self.index]
        #ADD IMAGE FLIPPING pygame.transform.flip(self.image, True, False)
    
    def interact(self, name):
        phrase = self.phrases_spoken[random.randint(0,len(self.phrases_spoken)-1)]
        try:
            phrase.replace('<name>', name)
        except:
            pass
        return phrase
    def mutter(self):
        phrase = self.random_phrases[random.randint(0,len(self.random_phrases)-1)]
        return phrase
    #Unfinished

    
