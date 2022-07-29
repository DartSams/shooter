import pygame
import math

class Player(pygame.sprite.Sprite):
    def __init__(self,x_pos,y_pos,image,lives):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = image
        self.lives = lives
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        # self.images = []
        # for num in range(1, 15):    
        #     # img = pygame.image.load(fr"ghost-pack\PNG\{self.sprite}\PNG Sequences\Dying\{self.sprite}_Dying_{num}.png")
        #     img = pygame.transform.scale(self.image, (100, 100))
        #     self.images.append(img)
        # self.index = 0
        # self.image = self.images[self.index]
        # self.rect = self.image.get_rect()
        # self.rect.center = [self.x_pos, self.y_pos]
        # self.counter = 0

    def draw(self,win):
        win.blit(self.image,(self.x_pos,self.y_pos))

    def collide(self,enemy):
        offset = (int(self.x_pos-enemy.x_pos),int(self.y_pos-enemy.y_pos))
        collided = enemy.mask.overlap(self.mask,offset)
        return collided