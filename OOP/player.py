import pygame
import math
import random
class Player(pygame.sprite.Sprite):
    def __init__(self,x_pos,y_pos,image,lives,selected_player):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.image = image
        self.lives = lives
        self.selected_player = selected_player
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.x_vel = random.randrange(1,9)
        self.y_vel = random.randrange(1,9)
        self.images = []
        for num in range(1, 12): #cycles through the folder of animations default is Idle    
            img = pygame.image.load(fr"ghost-pack\PNG\{self.selected_player}\PNG Sequences\Idle\{self.selected_player}_Idle_{num}.png")
            img = pygame.transform.scale(img, (100, 100))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x_pos, y_pos]
        self.counter = 0

    def draw(self,win):
        win.blit(self.image,(self.x_pos,self.y_pos))

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
