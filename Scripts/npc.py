import pygame
import os
import math
import random
class npc:
    def __init__(self, path, x, y):
        self.path = path
        self.animationIdle = []
        self.animationWalk = []
        self.x = x
        self.y = y
        self.xVel = 0
        self.coun = 0
        self.idle = True
        self.flip = True
        self.AIcount = 0
        for i in range(1, len(os.listdir(os.getcwd() + path+'/Idle'))+1):
            self.animationIdle.append(pygame.image.load(os.getcwd() + path + '/Idle/img{}.png'.format(i))) #PLEASE NAME THE IMAGES ACCORDINGLY 
        for i in range(1, len(os.listdir(os.getcwd() + path+'/Walk'))+1):
            self.animationWalk.append(pygame.image.load(os.getcwd() + path + '/Walk/img{}.png'.format(i))) #PLEASE NAME THE IMAGES ACCORDINGLY 
            

        self.counter = 0
    def display(self, screen):
        if not self.idle:
            if self.xVel > 0:
                self.flip = True
                screen.blit(pygame.transform.scale(pygame.transform.flip(self.animationWalk[int((self.counter//1))%6], True, False), (128, 128)), (self.x, self.y)) 
            else:
                self.flip = False
                screen.blit(pygame.transform.scale(self.animationWalk[int((self.counter//1))%6], (128, 128)), (self.x, self.y)) 
                
            
        else:
            if self.flip:
                screen.blit(pygame.transform.scale(pygame.transform.flip(self.animationIdle[int((self.counter//1))%6], True, False), (128, 128)), (self.x, self.y)) 
            else:
                screen.blit(pygame.transform.scale(self.animationIdle[int((self.counter//1))%6], (128, 128)), (self.x, self.y)) 
           
        self.counter += 1
    def AI(self):
        
        self.xVel = (random.randint(1, 15)*math.sin(self.AIcount/2)+random.randint(1, 15)*math.cos(self.AIcount)+random.randint(1, 15)*math.sin(3*self.AIcount/2))
        print(self.xVel)
        
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

        

    
    def update(self):
        self.x += self.xVel

    
 
        
        
        



