from numpy import place
import pygame
import random

class Target:
    def __init__(self,x_pos,y_pos,image,player):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = 20
        self.height = 20
        self.image = image
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self,win):
        win.blit(self.image,(self.x_pos,self.y_pos))
        # pygame.draw.rect(win,(255,255,0),[self.x_pos,self.y_pos,self.width,self.height])

    def target_hit(self,mask,x=0,y=0):
        bullet_mask = pygame.mask.from_surface(self.image)
        offset = (int(self.x_pos-x),int(self.y_pos-y))
        poi = mask.overlap(bullet_mask,offset)
        return poi
