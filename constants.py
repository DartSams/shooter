import pygame
import OOP
import random

from OOP import enemy

width,height = 700,700
win = pygame.display.set_mode((width,height))
pygame.font.init()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
velocity = 9
gravity = 2
starting_level = 1
player_health = 3
target_health = 100

selected_player = "Wraith_01" #sets the player sprite
selected_target = "Wraith_02" #sets the enemy sprite
player_right = pygame.image.load(rf"ghost-pack\PNG\{selected_player}\{selected_player}_Idle_000_right.png")
player_left = pygame.image.load(rf"ghost-pack\PNG\{selected_player}\{selected_player}_Idle_000_left.png")
target_image = pygame.image.load(rf"ghost-pack\PNG\{selected_target}\PNG Sequences\Idle\{selected_target}_Idle_1.png")
enemy_image = pygame.image.load(r"space-pack\PNG\Meteors\Meteor_03.png")
target = OOP.Target(random.randrange(0,width-100),random.randrange(0,height-100),target_image,target_health,selected_target) #creates a target object for player to shoot
player = OOP.Player(300,300,player_right,player_health,selected_player)
powerups = {
    "armor_bonus":{
        "image":pygame.image.load(r"space-pack\PNG\Bonus_Items\Armor_Bonus.png")
    },
    "damage_bonus":{
        "image":pygame.image.load(r"space-pack\PNG\Bonus_Items\Damage_Bonus.png")
    },
    "nuke":{
        "image":pygame.image.load(r"space-pack\PNG\Bonus_Items\Enemy_Destroy_Bonus.png")
    },
    "player_speed_debuff":{
        "image":pygame.image.load(r"space-pack\PNG\Bonus_Items\Hero_Movement_Debuff.png")
    },
    "player_health_bonus":{
        "image":pygame.image.load(r"space-pack\PNG\Bonus_Items\HP_Bonus.png")
    }
}   
arsenal = {
    "rocket":{
        "ammo":1,
        "image":pygame.image.load(r"gun-pack\2 Guns\10_1.png"),
        "bullet":pygame.image.load(r"gun-pack\5 Bullets\10.png"),
        "damage":20,
        "loadout":[]
    },
    "ak-47":{
        "ammo":10,
        "image":pygame.image.load(r"gun-pack\2 Guns\1_1.png"),
        "bullet":pygame.image.load(r"gun-pack\5 Bullets\1_2.png"),
        "damage":5,
        "loadout":[]
    }
}
selected_gun = "rocket" #sets the gun for the player to use


for name in arsenal.items(): #ccycles through all weapons in the arsenal dict to create a gun object for it and inserts in to the loadout of that weapon
    for i in range(2):
        name[1]["loadout"].append(OOP.Gun(player.x_pos,player.y_pos,arsenal[name[0]]["image"],arsenal[name[0]]["ammo"],arsenal[name[0]]["bullet"],player))
    # print(name[1]["loadout"])


gun_bullets = [] #list that holds the bullets
enemy_lst = [] #list that holds the enemies
player_lst = [] #list that holds the players


player_group = pygame.sprite.Group() #creates a sprite group for player animations
player_group.add(player) #adds the player object instance to the player group
death_group = pygame.sprite.Group() #creates a sprite group for death animations
target_group = pygame.sprite.Group() #creates a sprite group for target animations
target_group.add(target)

lvl = OOP.Level(starting_level,player_group,target_group,enemy_image)
lvl.start_level(enemy_image)