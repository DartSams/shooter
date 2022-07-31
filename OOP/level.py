import pygame
import random
import OOP

class Level:
    def __init__(self,width,height,level_num,player,target,enemy_image,arsenal):
        self.win_width = width
        self.win_height = height
        self.level_num = level_num
        self.current_level = 1
        self.playing = True
        self.run_game = False
        self.fps = 60
        self.clock = pygame.time.Clock() 
        self.time = 100
        self.time_str = str(self.time)
        self.enemy_amount = 30
        self.powerup_amount = 3
        self.enemy_lst = []
        self.powerup_lst = []
        self.gun_bullets = []
        self.player_group = player
        self.target_group = target
        self.enemy = enemy_image
        self.arsenal = arsenal
        self.score = 0
        self.max_score = 10
        self.endless_level = False 
        self.font = pygame.font.Font('freesansbold.ttf', 30)  
        self.score_text = self.font.render(f"Score: {str(self.score)}", True,(100, 100, 100))

    def increase_score(self):
        self.score = int(self.score) + 1
        self.score_text = self.font.render(f"Score: {str(self.score)}", True,(100, 100, 100))
        return self.score

    def start_level(self,enemy_image):
        self.draw_enemy(enemy_image,self.enemy_amount)

    def draw_guns(self):
        for name in self.arsenal.items(): #cycles through all weapons in the arsenal dict to create a gun object for it and inserts in to the loadout of that weapon
            for i in range(2):
                for player in self.player_group:
                    name[1]["loadout"].append(OOP.Gun(player.x_pos,player.y_pos,self.arsenal[name[0]]["image"],self.arsenal[name[0]]["ammo"],self.arsenal[name[0]]["bullet"],self.arsenal[name[0]]["full_auto"]))
            # print(name[1]["loadout"])


    def draw_enemy(self,image,amount):
        for i in range(amount + 1):
            self.enemy_lst.append(OOP.Enemy(random.randrange(0,self.win_width-4),random.randrange(-10000,0),image,"falling_enemy"))

    def draw_powerup(self):
        powerups = {
            "damage_bonus":{ #guns git increased damage
                "image":pygame.image.load(r"space-pack\PNG\Bonus_Items\Damage_Bonus.png"),
            },
            "nuke":{ #kill all enemies and targets on screen
                "image":pygame.image.load(r"space-pack\PNG\Bonus_Items\Enemy_Destroy_Bonus.png"),
            },
            "player_speed_debuff":{ #player moves slower
                "image":pygame.image.load(r"space-pack\PNG\Bonus_Items\Hero_Movement_Debuff.png"),
            },
            "player_health_bonus":{ #player get more lives
                "image":pygame.image.load(r"space-pack\PNG\Bonus_Items\HP_Bonus.png"),
            }
        }   
        # current_powerup_lst = [random.choice(list(powerups.keys())) for i in range(self.powerup_amount)]
        current_powerup_lst = [random.choice(list(powerups.keys())) for i in range(self.powerup_amount)]

        # print(current_powerup_lst)
        for item_name in current_powerup_lst:
            for i in range(self.powerup_amount + 1):
                self.powerup_lst.append(OOP.Enemy(random.randrange(0,self.win_width),random.randrange(-10000,0),powerups[item_name]["image"],item_name))

    
    def win_level(self): #called within every game loop iteration
        if self.endless_level == False: #sets the gamemode to be score based
            if self.score == self.max_score: #game ends
                print("You win")
                return False

            elif self.score != self.max_score: #game continous
                return True

        elif self.endless_level == True: #sets the gamemode to a endless survival 
            return True


    def lose_level(self): #called when player dies
        return False