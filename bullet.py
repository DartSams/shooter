import pygame


class Bullet:
    def __init__(self,gun):
        self.point = gun.head
        self.x_pos , self.y_pos = self.point
        self.width = 4
        self.height = 4
        self.cos = gun.cos
        self.sin = gun.sin
        self.x_vel = self.cos * 10 
        self.y_vel = self.sin * 10

    def move(self):
        self.x_pos += self.x_vel #increases the bullets x speed
        self.y_pos -= self.y_vel #increases the bullets y speed

    def draw(self,win):
        pygame.draw.rect(win,(255,0,0),[self.x_pos,self.y_pos,self.width,self.height]) 

