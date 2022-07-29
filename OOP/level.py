import pygame
import random
import OOP

class Level:
    def __init__(self,level_num):
        self.level_num = level_num
        self.playing = True
        self.fps = 60
        self.clock = pygame.time.Clock() 
        self.time = 10 
        self.time_str = "10"
        self.enemy_amount = 30
        self.enemy_lst = []
        self.score = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)  
        self.score_text = self.font.render(f"Score: {str(self.score)}", True,(255,255,255))

    def increase_score(self):
        self.score = int(self.score) + 1
        self.score_text = self.font.render(f"Score: {str(self.score)}", True,(255,255,255))
        return self.score

    def decrement_timer(self):
        milliseconds = self.time * 100
        for i in range(milliseconds):
            milliseconds -= 1
            if milliseconds % 100:
                self.time = int(self.time) - 1
                self.timer_text = self.font.render(f"{str(self.time)}s", True,(255,255,255))
                return self.time

    def start_level(self):
        self.draw_enemy() 

    def draw_enemy(self):
        for i in range(self.enemy_amount + 1):
            self.enemy_lst.append(OOP.Enemy(random.randrange(0,700-4),random.randrange(-10000,0)))

    def win_level(self):
        pass

    def lose_level(self):
        return False