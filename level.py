import pygame
from enemy import Enemy
import random

class Level:
    def __init__(self,level_num):
        self.level_num = level_num
        self.time = 10
        self.enemy_amount = 30
        self.enemy_lst = []

    def draw_enemy(self):
        for i in range(self.enemy_amount):
            self.enemy_lst.append(Enemy(random.randrange(0,700),random.randrange(-100,0)))

    def win_level(self):
        pass

    def lose_level(self):
        pass