import pygame
import math
player_x = 100
player_y = 100
class Gun:
    def __init__(self,x_pos,y_pos,image,ammo,player):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = image
        self.ammo = ammo
        self.player = player
        self.image = pygame.transform.scale2x(self.image)

    def shoot(self):
        self.ammo -= 1

    def draw(self,win):
        # win.blit(self.image,(self.x_pos,self.y_pos))
        angle = 360-math.atan2(pygame.mouse.get_pos()[1]-self.player.y_pos,pygame.mouse.get_pos()[0]-self.player.x_pos)*180/math.pi
        rotimage = pygame.transform.rotate(self.image,angle)
        rect = rotimage.get_rect(center=(self.x_pos,self.y_pos))
        win.blit(rotimage,rect) #I need space_ship to rotate towards my cursor

