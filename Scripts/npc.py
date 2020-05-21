import pygame
import os
import math
import random
class npc(pygame.sprite.Sprite):
    def __init__(self, path, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.path = path
        self.animationIdle = []
        self.animationWalk = []
        
        self.xVel = 0
        self.coun = 0
        self.idle = True
        self.flip = True
        self.AIcount = 0

        self.image = pygame.image.load(os.getcwd()+ path+'/Idle/DAN-1.png')
        self.image = pygame.transform.scale(self.image, (128, 128))


        for i in range(1, len(os.listdir(os.getcwd() + path+'/Idle'))+1):
            self.animationIdle.append(pygame.image.load(os.getcwd() + path + '/Idle/DAN-{}.png'.format(i))) #PLEASE NAME THE IMAGES ACCORDINGLY 
        for i in range(1, len(os.listdir(os.getcwd() + path+'/Walk'))+1):
            self.animationWalk.append(pygame.image.load(os.getcwd() + path + '/Walk/DANWalk-{}.png'.format(i))) #PLEASE NAME THE IMAGES ACCORDINGLY 
        
        self.rect = self.image.get_rect(center=[x, y])
        self.rect.center = (x, y)

        self.rect.x = x
        self.rect.y = y

        self.counter = 0
    def display(self, screen):
        if not self.idle:
            if self.xVel > 0:
                self.flip = True
                self.image = pygame.transform.scale(pygame.transform.flip(self.animationWalk[int((self.counter//1))%6], True, False), (128, 128))
            if self.xVel<0:
                self.flip = False
                self.image = pygame.transform.scale(self.animationWalk[int((self.counter//1))%6], (128, 128))
                
            
        else:
            if self.flip:
                self.image = pygame.transform.scale(pygame.transform.flip(self.animationIdle[int((self.counter//1))%6], True, False), (128, 128))
            else:
                self.image = pygame.transform.scale(self.animationIdle[int((self.counter//1))%6], (128, 128))
           
        self.counter += 1
    def AI(self):
        
        self.xVel = (random.randint(1, 15)*math.sin(self.AIcount/2)+random.randint(1, 15)*math.cos(self.AIcount)+random.randint(1, 15)*math.sin(3*self.AIcount/2))
        
        
        if self.xVel > 8:
            self.xVel = 12
            self.idle = False
        elif self.xVel < -8:
            self.xVel = -12
            self.idle = False
        else:
            self.xVel = 0
            self.idle = True
    
        self.AIcount += 0.07

        
    
        
    
    def update(self, screen):
        self.rect.x += self.xVel
        self.display(screen)
        self.AI()

    
 
        
        
        




        
        



