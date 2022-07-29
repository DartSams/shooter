import pygame
from gun import Gun
from player import Player
from bullet import Bullet
from enemy import Enemy
from level import Level
from target import Target
import random

width,height = 700,700
fps = 60
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
playing = True
velocity = 5
gravity = 4
rocket_image = pygame.image.load(r"gun-pack\2 Guns\10_1.png")
player_right = pygame.image.load(r"ghost-pack\PNG\Wraith_03\PNG Sequences\Idle\Wraith_03_Idle_000_right.png")
player_left = pygame.image.load(r"ghost-pack\PNG\Wraith_03\PNG Sequences\Idle\Wraith_03_Idle_000_left.png")
player = Player(300,300,player_right,3)
target_image = pygame.image.load(r"ghost-pack\PNG\Wraith_03\PNG Sequences\Idle\Wraith_03_Idle_001.png")
clock = pygame.time.Clock()
starting_level = 1
# lvl = Level(starting_level)

arsenal = {
    "rocket":{
        "ammo":1,
        "image":pygame.image.load(r"gun-pack\2 Guns\10_1.png"),
        "bullet":pygame.image.load(r"gun-pack\5 Bullets\10.png")
    },
    "ak-47":{
        "ammo":10,
        "image":pygame.image.load(r"gun-pack\2 Guns\1_1.png"),
        "bullet":pygame.image.load(r"gun-pack\5 Bullets\1_2.png")
    }
}

rocket = Gun(player.x_pos,player.y_pos,arsenal["rocket"]["image"],arsenal["rocket"]["ammo"],arsenal["rocket"]["bullet"],player)
rocket2 = Gun(player.x_pos,player.y_pos,arsenal["rocket"]["image"],arsenal["rocket"]["ammo"],arsenal["rocket"]["bullet"],player)
ak47 = Gun(player.x_pos,player.y_pos,arsenal["ak-47"]["image"],arsenal["ak-47"]["ammo"],arsenal["ak-47"]["bullet"],player)
ak472 = Gun(player.x_pos,player.y_pos,arsenal["ak-47"]["image"],arsenal["ak-47"]["ammo"],arsenal["ak-47"]["bullet"],player)
gun_bullets = []
loadout = [rocket,rocket2]
enemy_lst = []
enemy_group = pygame.sprite.Group()

# loadout = [ak47,ak472]

for i in range(30):
    enemy_lst.append(Enemy(random.randrange(0,width-4),random.randrange(-10000,0)))
target = Target(random.randrange(0,width-100),random.randrange(0,height-100),target_image)

death_group = pygame.sprite.Group()