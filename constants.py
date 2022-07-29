import pygame
import OOP
import random

width,height = 700,700
win = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()   
fps = 60
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
playing = True
velocity = 5
gravity = 4
selected_gun = "rocket" #sets the gun for the player to use
selected_player = "Wraith_03" #sets the player sprite
selected_enemy = "Wraith_01" #sets the enemy sprite
player_right = pygame.image.load(rf"ghost-pack\PNG\{selected_player}\{selected_player}_Idle_000_right.png")
player_left = pygame.image.load(rf"ghost-pack\PNG\{selected_player}\{selected_player}_Idle_000_left.png")
target_image = pygame.image.load(rf"ghost-pack\PNG\{selected_enemy}\PNG Sequences\Idle\{selected_enemy}_Idle_1.png")
target = OOP.Target(random.randrange(0,width-100),random.randrange(0,height-100),target_image) #creates a target object for player to shoot
player = OOP.Player(300,300,player_right,3)

arsenal = {
    "rocket":{
        "ammo":1,
        "image":pygame.image.load(r"gun-pack\2 Guns\10_1.png"),
        "bullet":pygame.image.load(r"gun-pack\5 Bullets\10.png"),
        "loadout":[]
    },
    "ak-47":{
        "ammo":10,
        "image":pygame.image.load(r"gun-pack\2 Guns\1_1.png"),
        "bullet":pygame.image.load(r"gun-pack\5 Bullets\1_2.png"),
        "loadout":[]
    }
}



for name in arsenal.items(): 
    for i in range(2):
        name[1]["loadout"].append(OOP.Gun(player.x_pos,player.y_pos,arsenal[name[0]]["image"],arsenal[name[0]]["ammo"],arsenal[name[0]]["bullet"],player))
    # print(name[1]["loadout"])


gun_bullets = [] #list that holds the bullets
enemy_lst = [] #list that holds the enemies
player_lst = [] #list that holds the players

for i in range(30+1): #creates 30 enemy objects to attack the player
    enemy_lst.append(OOP.Enemy(random.randrange(0,width-4),random.randrange(-10000,0)))

player_group = pygame.sprite.Group() #creates a sprite group for player animations
player_group.add(player) #adds the player object instance to the player group
death_group = pygame.sprite.Group() #creates a sprite group for death animations
target_group = pygame.sprite.Group() #creates a sprite group for target animations
target_group.add(target)