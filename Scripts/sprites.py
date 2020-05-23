import random
import math
import pygame, sys
import os
from pygame.locals import *
from lvl import *


#Every important character will have its own class for logic stuff.
#Vee is the *ONLY* playable class
class Vee(pygame.sprite.Sprite):
    def __init__(self):
        super(Vee, self).__init__()
        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        self.frame = 0

        self.jcount = 0

        self.ycollide = False
        self.xcollide = False

        self.yvel = 0

        self.speed = 10 #pixels per cycle

        self.images_walk = []
        self.image = pygame.image.load(os.path.dirname(os.getcwd())+'/Assets/Characters/Playable/Vee/Idle/'+'VEEE_Idle-1.png')
        self.image=pygame.transform.scale(self.image,(128,128))
        
        self.last = ''
        for i in range (1,5): #walk
            self.images_walk.append(pygame.image.load(os.path.dirname(os.getcwd())+'/Assets/Characters/Playable/Vee/Walk/'+'VEEE_walk-'+str(i)+'.png'))
        self.images_idle = []
        for i in range (1,6): #idle
            self.images_idle.append(pygame.image.load(os.path.dirname(os.getcwd())+'/Assets/Characters/Playable/Vee/Idle/'+'VEEE_Idle-'+str(i)+'.png'))

        self.index = 0 #for sprite animations
        self.location = [100,250]
        
        self.rect = self.image.get_rect(center=self.location)

        self.rect.x = self.location[0]
        self.rect.y = self.location[1]

        self.health = 100
        self.random_phrases = ['Inilaute Amma', 'By meaning?'] #Random mutterings
        self.phrases_spoken = ['Sexy ass, <name> ah','Shut up', 'Shut up, <name>', 'EEEH', 
                                'ITS YOUR FAULT!', 'EEEEH', 'Eh, you ah!', 'YOU DID IT!', 'Do you want to be belted, <name>?', 'YOU FUCCKKING DID IT!!'] #directed at people
    
    def checkFloorCollison(self):
        if self.rect.y > 768-128:
            self.ycollide = True
            self.rect.y = 768-128
        if self.rect.y < 768-128:
            self.ycollide = False
        self.location[1] = self.rect.y
    '''
    def checkTileCollision(self):
        for y in range(0,12): #tile collision based on tile map
            for x in range(0,20):
                coord = level[y][x]
                if coord > 0:
                    if self.location[1] >= y*64-128:
                        self.ycollide = True
                    if self.location[1] < y*64-128:
                        self.ycollide = False
                if coord == 0:
                    self.ycollide = False
        self.location[1] = 
    '''
    def checkTileCollision(self):
        maploc = [round((self.location[0]+45)/64),round((self.location[1]+160)/64)] #mapping location to tile space
        coord = level[maploc[1]-1][maploc[0]]
        if coord > 0:
            self.ycollide = True
            self.rect.y = maploc[1]*64-190
        print (maploc[1]*64)

    def update(self,l, r, j):
        self.checkFloorCollison()
        #print(self.ycollide)
        self.checkTileCollision()

        if self.ycollide == False:
            j = False

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
        
        if j == True and self.jcount < 2:
            self.jcount += 1
            self.index += 1
            self.yvel = 24
            if self.index >= len(self.images_idle)-1: #Jump implementation
                self.index = len(self.images_idle)-1
            self.image=self.images_idle[self.index]
            if self.last == 'r':
                self.image=self.images_idle[self.index]
                self.image=pygame.transform.flip(self.image, True, False)
            else:
                self.image=self.images_idle[self.index]
            j == False
            

        if r == False and l == False and j == False and self.jcount < 2 and self.ycollide == True:
            self.index += 1
            if self.index >= len(self.images_idle)-1: #idle cycle
                self.index = 0
            if self.last == 'r':
                self.image=self.images_idle[self.index]
                self.image=pygame.transform.flip(self.image, True, False)
            else:
                self.image=self.images_idle[self.index]

        self.image=pygame.transform.scale(self.image,(128,128)) #upscale

        if self.ycollide == True:
            self.jcount = 0
        if self.ycollide == False and j==False:
            self.yvel -= 4
            #print(self.yvel)
            
        if self.ycollide == True and j==False:
            self.yvel = 0
        #print(self.rect.y)
        self.rect.y -= self.yvel
        self.location[1] = self.rect.y
        

    def mutter(self):
        phrase = self.random_phrases[random.randint(0,len(self.random_phrases)-1)]
        return phrase
    #Unfinished

################################
# NPCs go below this comment   #
################################

class Odd(pygame.sprite.Sprite):
    def __init__(self):
        super(Odd, self).__init__()
        self.movex = 0 # move along X
        self.movey = 0 # move along Y
        self.frame = 0
        self.count = 0
        self.di = 0 #state bool

        self.speed = 10 #pixels per cycle

        self.image = pygame.image.load(os.path.dirname(os.getcwd())+'/Assets/Characters/NPC/MrOdd/Walk/Hover/'+'OddHover-1.png')
        self.image=pygame.transform.scale(self.image,(128,128))
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

        self.rect = self.image.get_rect(center=self.location)
        self.rect.center = (250, 250)

        self.rect.x = self.location[0]
        self.rect.y = self.location[1]

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