import pygame
import random

class Target(pygame.sprite.Sprite):
    def __init__(self,x_pos,y_pos,image,target_health,selected_target):
        pygame.sprite.Sprite.__init__(self)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = 20
        self.height = 20
        self.image = image
        self.target_health_image = pygame.image.load(r"space-pack\PNG\Bonus_Items\heart.png")
        self.target_health_image = pygame.transform.scale(self.target_health_image,(20,20))
        self.target_health = []
        self.target_health_offset = target_health * 2 #this is needed beacuse there are 2 guns shooting at 1 target so the target will need double health
        self.healthbar_width = 90 
        self.selected_target = selected_target
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.mask = pygame.mask.from_surface(self.image)
        self.images = []
        [self.target_health.append(self.target_health_image) for i in range(3)]
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

        # win.blit(self.target_health[0],(self.x_pos+30,self.y_pos+self.height))
        # win.blit(self.target_health[1],(self.x_pos+60,self.y_pos+self.height))
        # win.blit(self.target_health[2],(self.x_pos+90,self.y_pos+self.height))
        # offset = 30
        # for i in range(3):
        #     win.blit(self.target_health[i],(self.x_pos+offset,self.y_pos+self.height))
        #     offset += 30
        # x = pygame.Rect(self.x_pos,self.y_pos+self.height-10,self.width,10)
        # win.blit(x)
        self.heathbar_holder = pygame.draw.rect(win,(255,0,0),[self.x_pos,self.y_pos+self.height-10,90,10])
        self.heathbar = pygame.draw.rect(win,(0,255,0),[self.x_pos,self.y_pos+self.height-10,self.healthbar_width ,10])
        # self.heathbar_rect = self.heathbar.get_rect()

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
