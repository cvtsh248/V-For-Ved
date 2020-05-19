import random
import math
import pygame, sys
import os
from pygame.locals import *

#Every important character will have its own class for logic stuff.
#Vee is the *ONLY* playable class
class Vee(pygame.sprite.Sprite):
    def __init__(self):
        super(Vee, self).__init__()
        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        self.frame = 0

        self.speed = 10 #pixels per cycle

        self.images_walk = []
        self.last = ''
        for i in range (1,5): #walk
            self.images_walk.append(pygame.image.load(os.path.dirname(os.getcwd())+'/Assets/Characters/Playable/Vee/Walk/'+'VEEE_walk-'+str(i)+'.png'))
        self.images_idle = []
        for i in range (1,6): #idle
            self.images_idle.append(pygame.image.load(os.path.dirname(os.getcwd())+'/Assets/Characters/Playable/Vee/Idle/'+'VEEE_Idle-'+str(i)+'.png'))
        #Image and animation stuff to be added

        self.index = 0 #for sprite animations
        self.location = [250,250]

        self.rect = pygame.Rect(5, 5, 32, 32)
        self.rect.center = (250, 250)

        self.health = 100
        self.random_phrases = ['Inilaute Amma', 'By meaning?'] #Random mutterings
        self.phrases_spoken = ['Sexy ass, <name> ah','Shut up', 'Shut up, <name>', 'EEEH', 
                                'ITS YOUR FAULT!', 'EEEEH', 'Eh, you ah!', 'YOU DID IT!', 'Do you want to be belted, <name>?'] #directed at people
    def update(self,l, r, j):
        
        if l == True and r == False:
            self.last = 'l'
            self.location[0]-=self.speed
            self.rect.x -= self.speed
            if j == False:
                self.index += 1
                if self.index >= len(self.images_walk)-1: #walk cycles
                    self.index = 0
                self.image=self.images_walk[self.index]

        if r == True and l == False:
            self.last = 'r'
            self.location[0]+= self.speed
            self.rect.x += self.speed
            if j == False:
                self.index += 1
                if self.index >= len(self.images_walk)-1: #walk cycle
                    self.index = 0
                self.image=self.images_walk[self.index]
            self.image=pygame.transform.flip(self.image, True, False)
        
        if j == True:
            self.index += 1
            if self.index >= len(self.images_idle)-3: #Jump implementation
                self.index = len(self.images_idle)-3
            self.image=self.images_idle[self.index]
            if self.last == 'r':
                self.image=self.images_idle[self.index]
                self.image=pygame.transform.flip(self.image, True, False)
            else:
                self.image=self.images_idle[self.index]
        

        if r == False and l == False and j == False:
            self.index += 1
            if self.index >= len(self.images_idle)-1: #idle cycle
                self.index = 0
            if self.last == 'r':
                self.image=self.images_idle[self.index]
                self.image=pygame.transform.flip(self.image, True, False)
            else:
                self.image=self.images_idle[self.index]

        self.image=pygame.transform.scale(self.image,(128,128)) #upscaladd
        phrase = self.phrases_spoken[random.randint(0,len(self.phrases_spoken)-1)]

    def mutter(self):
        phrase = self.random_phrases[random.randint(0,len(self.random_phrases)-1)]
        return phrase
    #Unfinished

# NPCs go below this comment
class Odd(pygame.sprite.Sprite):
    def __init__(self):
        super(Odd, self).__init__()
        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        self.frame = 0
        self.count = 0
        self.di = 0 #state bool

        self.speed = 10 #pixels per cycle

        self.images_walk = []
        self.last = ''
        for i in range (1,9): #hover
            self.images_walk.append(pygame.image.load(os.path.dirname(os.getcwd())+'/Assets/Characters/NPC/MrOdd/Walk/Hover/'+'OddHover-'+str(i)+'.png'))
        
        self.images_idle_shine = []
        for i in range (1,13): #Shine idle
            self.images_idle_shine.append(pygame.image.load(os.path.dirname(os.getcwd())+'/Assets/Characters/NPC/MrOdd/Idle/Shine/'+'OddShine-'+str(i)+'.png'))

        
        #Image and animation stuff to be added

        self.index = 0 #for sprite animations
        self.location = [250,250]

        self.rect = pygame.Rect(5, 5, 32, 32)
        self.rect.center = (250, 250)

        self.health = 100
        '''
        self.random_phrases = ['Inilaute Amma', 'By meaning?'] #Random mutterings
        self.phrases_spoken = ['Sexy ass, <name> ah','Shut up', 'Shut up, <name>', 'EEEH', 
                                'ITS YOUR FAULT!', 'EEEEH', 'Eh, you ah!', 'YOU DID IT!', 'Do you want to be belted, <name>?'] #directed at people
        '''
    def update(self):
        self.count += 1
        if self.count == 1:
            self.di = 300
        if self.count%4 == 0:
            self.di = random.randint(-300,300)
        L = False
        R = False
        if self.di > -100 and self.di < -50:
            L = True
            R = False
        if self.di > -50 and self.di < 50:
            L = False
            R = False
        if self.di > 50 and self.di < 100:
            L = False
            R = True

        if L == True:
            self.last = 'l'
            self.location[0]-=self.speed
            self.index += 1
            self.rect.x -= self.speed
            if self.index >= len(self.images_walk)-1: #walk cycles
                self.index = len(self.images_walk)-1
            self.image=self.images_walk[self.index]           

        if R == True:
            self.last = 'r'
            self.location[0]+= self.speed
            self.index += 1
            self.rect.x += self.speed
            if self.index >= len(self.images_walk)-1: #walk cycle
                self.index = len(self.images_walk)-1
            self.image=self.images_walk[self.index]
            self.image=pygame.transform.flip(self.image, True, False)

        if L == False and R == False:
            self.index += 1
            if self.index >= len(self.images_idle_shine)-1: #idle cycle
                self.index = 0
            if self.last == 'r':
                self.image=self.images_idle_shine[self.index]
                self.image=pygame.transform.flip(self.image, True, False)
            else:
                self.image=self.images_idle_shine[self.index]

        self.image=pygame.transform.scale(self.image,(128,128)) #upscale