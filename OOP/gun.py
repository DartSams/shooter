import pygame
import math
import OOP

class Gun:
    def __init__(self,x_pos,y_pos,image,ammo,bullet_type,machine_type):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.ammo = ammo
        self.original_clip = ammo
        self.full_auto = machine_type
        self.bullet_type = bullet_type
        self.bullet_group = pygame.sprite.Group()
        self.image = pygame.transform.scale2x(self.image)
        self.rotimage = 0
        self.angle = 0
        self.cos = math.cos(math.radians(self.angle))
        self.sin = math.sin(math.radians(self.angle))
        self.head = (self.x_pos +  self.cos * self.width//2,self.y_pos - self.sin * self.height//2)

    def shoot(self,gun_lst):
        # print(gun_lst)
        shot = OOP.Bullet(self)
        if self.ammo <= 0 or self.full_auto==True: #stops from non stop firing rockets shouldnt have full auto
            gun_lst.append(shot)
            # self.bullet_group.add(shot)
        self.ammo -= 1        
        

    def draw(self,win):
        # win.blit(self.image,(self.x_pos,self.y_pos))
        self.angle = 360-math.atan2(pygame.mouse.get_pos()[1]-self.y_pos,pygame.mouse.get_pos()[0]-self.x_pos)*180/math.pi 
        self.rotimage = pygame.transform.rotate(self.image,self.angle) #rotates the image with the given angle
        self.rect = self.rotimage.get_rect(center=(self.x_pos,self.y_pos))
        win.blit(self.rotimage,self.rect) #I need space_ship to rotate towards my cursor
        self.cos = math.cos(math.radians(self.angle))
        self.sin = math.sin(math.radians(self.angle))
        self.head = (self.x_pos +  self.cos * self.width//2,self.y_pos - self.sin * self.height//2)
