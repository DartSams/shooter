import pygame
import random

class Target(pygame.sprite.Sprite):
    def __init__(self,x_pos,y_pos,image,selected_target):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = 20
        self.height = 20
        self.image = image
        self.selected_target = selected_target
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.images = []
        for num in range(1, 12): #cycles through the folder of animations default is Idle  
            img = pygame.image.load(fr"ghost-pack\PNG\{self.selected_target}\PNG Sequences\Idle\{self.selected_target}_Idle_{num}.png")
            img = pygame.transform.scale(img, (100, 100))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x_pos, y_pos]
        self.counter = 0

    def draw(self,win):
        win.blit(self.image,(self.x_pos,self.y_pos))
        # pygame.draw.rect(win,(255,255,0),[self.x_pos,self.y_pos,self.width,self.height])

    def hit(self,enemy):
        offset = (int(self.x_pos-enemy.x_pos),int(self.y_pos-enemy.y_pos))
        collided = enemy.mask.overlap(self.mask,offset)
        return collided

    def update(self): #cycles through the Idle animation
        death_speed = 4 
        self.counter += 1

        if self.counter >= death_speed and self.index < len(self.images) - 1: #updates the current image
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        #if the animation is complete, reset animation index
        if self.index >= len(self.images) - 1 and self.counter >= death_speed: #resets the animation back to the beginning for a endless animation set
            self.counter = 0
            self.index = 0
            self.image = self.images[self.index]
