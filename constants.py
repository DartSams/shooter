import pygame
import OOP
import random

width,height = 500,500
win = pygame.display.set_mode((width,height))
pygame.font.init()
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
grey = (100, 100, 100)
velocity = 9
gravity = 2
starting_level = 1
player_health = 3
target_health = 100

sprites = ["Wraith_01","Wraith_02","Wraith_03"]
selected_player = "Wraith_01" #sets the player sprite
# selected_target = "Wraith_03" #sets the enemy sprite
selected_target = random.choice(sprites) #sets the enemy sprite to random 
player_right = pygame.image.load(rf"ghost-pack\PNG\{selected_player}\{selected_player}_Idle_000_right.png")
player_left = pygame.image.load(rf"ghost-pack\PNG\{selected_player}\{selected_player}_Idle_000_left.png")
target_image = pygame.image.load(rf"ghost-pack\PNG\{selected_target}\PNG Sequences\Idle\{selected_target}_Idle_1.png")
enemy_image = pygame.image.load(r"space-pack\PNG\Meteors\Meteor_03.png")
health_image = pygame.image.load(r"space-pack\PNG\Bonus_Items\heart.png")
health_image = pygame.transform.scale(health_image,(50,50))
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
    "ak-47":{
        "ammo":60,
        "image":pygame.image.load(r"gun-pack\2 Guns\1_1.png"),
        "bullet":pygame.image.load(r"gun-pack\5 Bullets\1.png"),
        "damage":5,
        "full_auto":False,
        "loadout":[]
    },
    "shotgun":{
        "ammo":10,
        "image":pygame.image.load(r"gun-pack\2 Guns\2_1.png"),
        "bullet":pygame.image.load(r"gun-pack\5 Bullets\2.png"),
        "damage":40,
        "full_auto":False,
        "loadout":[]
    },
    "laser":{
        "ammo":200,
        "image":pygame.image.load(r"gun-pack\2 Guns\3_1.png"),
        "bullet":pygame.image.load(r"gun-pack\5 Bullets\3.png"),
        "damage":5,
        "full_auto":True,
        "loadout":[]
    },
    "blaster":{
        "ammo":10,
        "image":pygame.image.load(r"gun-pack\2 Guns\4_1.png"),
        "bullet":pygame.image.load(r"gun-pack\5 Bullets\4.png"),
        "damage":5,
        "full_auto":False,
        "loadout":[]
    },
    "sniper-rocket":{
        "ammo":3,
        "image":pygame.image.load(r"gun-pack\2 Guns\5_1.png"),
        "bullet":pygame.image.load(r"gun-pack\5 Bullets\5.png"),
        "damage":50,
        "full_auto":False,
        "loadout":[]
    },
    "sniper":{
        "ammo":8,
        "image":pygame.image.load(r"gun-pack\2 Guns\6_1.png"),
        "bullet":pygame.image.load(r"gun-pack\5 Bullets\6.png"),
        "damage":40,
        "full_auto":False,
        "loadout":[]
    },
    "needle":{
        "ammo":100,
        "image":pygame.image.load(r"gun-pack\2 Guns\7_1.png"),
        "bullet":pygame.image.load(r"gun-pack\5 Bullets\7.png"),
        "damage":20,
        "full_auto":True,
        "loadout":[]
    },
    "railgun":{
        "ammo":2,
        "image":pygame.image.load(r"gun-pack\2 Guns\8_1.png"),
        "bullet":pygame.image.load(r"gun-pack\5 Bullets\8.png"),
        "damage":50,
        "full_auto":False,
        "loadout":[]
    },
    "mp5":{
        "ammo":10,
        "image":pygame.image.load(r"gun-pack\2 Guns\9_1.png"),
        "bullet":pygame.image.load(r"gun-pack\5 Bullets\9.png"),
        "damage":10,
        "full_auto":False,
        "loadout":[]
    },
    "rocket":{
        "ammo":1,
        "image":pygame.image.load(r"gun-pack\2 Guns\10_1.png"),
        "bullet":pygame.image.load(r"gun-pack\5 Bullets\10.png"),
        "damage":50,
        "full_auto":False,
        "loadout":[]
    }
}
possible_guns = list(arsenal.keys())
# selected_gun = "sniper-rocket" #sets the gun for the player to use
selected_gun = random.choice(possible_guns)
for name in arsenal.items(): #ccycles through all weapons in the arsenal dict to create a gun object for it and inserts in to the loadout of that weapon
    for i in range(2):
        name[1]["loadout"].append(OOP.Gun(player.x_pos,player.y_pos,arsenal[name[0]]["image"],arsenal[name[0]]["ammo"],arsenal[name[0]]["bullet"],arsenal[name[0]]["full_auto"]))
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