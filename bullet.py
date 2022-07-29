import pygame


class Bullet:
    def __init__(self,gun):
        self.image = gun.bullet_type
        self.rect = self.image.get_rect()
        self.point = gun.head
        self.x_pos , self.y_pos = self.point
        self.width = 4
        self.height = 4
        self.cos = gun.cos
        self.sin = gun.sin
        self.x_vel = self.cos * 10 
        self.y_vel = self.sin * 10
        self.sprite = pygame.sprite.Sprite()
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        self.x_pos += self.x_vel #increases the bullets x speed
        self.y_pos -= self.y_vel #increases the bullets y speed

    def draw(self,win):
        win.blit(self.image,(self.x_pos,self.y_pos))
        # pygame.draw.rect(win,(255,0,0),[self.x_pos,self.y_pos,self.width,self.height]) 

    def collide(self,enemy):
        offset = (int(self.x_pos-enemy.x_pos),int(self.y_pos-enemy.y_pos))
        collided = enemy.mask.overlap(self.mask,offset)
        return collided