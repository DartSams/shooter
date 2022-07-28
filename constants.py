import pygame
from gun import Gun
from player import Player
from bullet import Bullet

width,height = 700,700
fps = 60
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
playing = True
velocity = 2
rocket_image = pygame.image.load(r"gun-pack\2 Guns\10_1.png")
player_right = pygame.image.load(r"ghost-pack\PNG\Wraith_03\PNG Sequences\Idle\Wraith_03_Idle_000_right.png")
player_left = pygame.image.load(r"ghost-pack\PNG\Wraith_03\PNG Sequences\Idle\Wraith_03_Idle_000_left.png")
player = Player(300,300,player_right,3)
clock = pygame.time.Clock()



arsenal = {
    "rocket":{
        "ammo":1,
        "image":pygame.image.load(r"gun-pack\2 Guns\10_1.png"),
        "bullet":pygame.image.load(r"gun-pack\5 Bullets\10.png")
    }
}

rocket = Gun(player.x_pos,player.y_pos,arsenal["rocket"]["image"],arsenal["rocket"]["ammo"],arsenal["rocket"]["bullet"],player)
rocket2 = Gun(player.x_pos,player.y_pos,arsenal["rocket"]["image"],arsenal["rocket"]["ammo"],arsenal["rocket"]["bullet"],player)
gun_bullets = []
loadout = [rocket,rocket2]