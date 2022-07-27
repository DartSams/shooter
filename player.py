import pygame
import math
player_x = 300
player_y = 300
width,height = 700,700
class Player:
    def __init__(self,x_pos,y_pos,image,lives):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = image
        self.lives = lives
        self.image = pygame.transform.scale(self.image,(100,100))
        self.facing = "left"

    def draw(self,win):
        win.blit(self.image,(self.x_pos,self.y_pos))