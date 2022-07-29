import pygame

class Enemy:
    def __init__(self,x_pos,y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = 4
        self.height = 4
        self.image = pygame.image.load(r"space-pack\PNG\Meteors\Meteor_03.png")
        self.image = pygame.transform.scale(self.image,(30,30))
        self.mask = pygame.mask.from_surface(self.image)

    def draw(self,win):
        win.blit(self.image,(self.x_pos,self.y_pos))

    def hit(self,enemy):
        offset = (int(self.x_pos-enemy.x_pos),int(self.y_pos-enemy.y_pos))
        collided = enemy.mask.overlap(self.mask,offset)
        return collided
