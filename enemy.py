import pygame

class Enemy:
    def __init__(self,x_pos,y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = 4
        self.height = 4


    def draw(self,win):
        self.rect = pygame.draw.rect(win,(255,0,0),[self.x_pos,self.y_pos,self.width,self.height])

    