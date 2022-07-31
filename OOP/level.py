import pygame
import random
import OOP

class Level:
    def __init__(self,level_num,player,target,enemy_image):
        self.level_num = level_num
        self.current_level = 1
        self.playing = True
        self.fps = 60
        self.clock = pygame.time.Clock() 
        self.time = 30
        self.time_str = str(self.time)
        self.enemy_amount = 30
        self.enemy_lst = []
        self.player = player
        self.target = target
        self.enemy = enemy_image
        self.score = 0
        self.max_score = 10
        self.font = pygame.font.Font('freesansbold.ttf', 32)  
        self.score_text = self.font.render(f"Score: {str(self.score)}", True,(255,255,255))

    def increase_score(self):
        self.score = int(self.score) + 1
        self.score_text = self.font.render(f"Score: {str(self.score)}", True,(255,255,255))
        return self.score

    def start_level(self,enemy_image):
        self.draw_enemy(enemy_image)

    def draw_enemy(self,enemy_image):
        for i in range(self.enemy_amount + 1):
            self.enemy_lst.append(OOP.Enemy(random.randrange(0,700-4),random.randrange(-10000,0),enemy_image))

    def win_level(self): #called within every game loop iteration
        if self.score == self.max_score: #game ends
            print("You win")
            return False

        elif self.score != self.max_score: #game continous
            return True


    def lose_level(self): #called when player dies
        return False