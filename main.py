import pygame
from constants import *
import OOP

pygame.init()
pygame.display.set_caption("Shooter")
pygame.time.set_timer(pygame.USEREVENT, 1000)
while lvl.playing:
    lvl.clock.tick(lvl.fps)
    lvl.playing = lvl.win_level() #on each game loop sets the playing state to be True or False based on the players progress

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lvl.playing = False 
            break

        if event.type == pygame.USEREVENT: #decrements the set timer in each game loop 
            lvl.time -= 1
            lvl.time_str = str(lvl.time) 
            if lvl.time > 0: #while there is still time left
                pass
            elif lvl.time <= 0: #when level timer reaches 0 then 
                print("Time ran out")
                lvl.playing = lvl.lose_level()
            # print(lvl.text)

        if event.type == pygame.KEYDOWN: #detects any keyboard key presses
            if event.key == pygame.K_SPACE: #if spacebar is pressed shoots a bullet
                for i in arsenal[selected_gun]["loadout"]:
                    i.shoot(gun_bullets)

    if arsenal[selected_gun]["full_auto"] == True: #checks if the current gun has a full_auto feature
        if pygame.mouse.get_pressed() == (1, 0, 0): #checks if left mouse button is pressed if True or 1 shoots a endless supply of bullet objects while held down
            for i in arsenal[selected_gun]["loadout"]:
                i.shoot(gun_bullets)

    keys = pygame.key.get_pressed() #detecting multiple keys at once
    if keys[pygame.K_d]: #moves right
        player.x_pos += velocity
        player.image = pygame.transform.scale(player_right,(100,100)) #changes the orientation of the image to the right

    if keys[pygame.K_a]:#moves left
        player.x_pos -= velocity
        player.image = pygame.transform.scale(player_left,(100,100)) #changes the orientation of the image to the left
    if keys[pygame.K_w]:#moves up
        player.y_pos -= velocity

    if keys[pygame.K_s]:#moves down
        player.y_pos += velocity

    for i in gun_bullets: #when there are bullets in the list draws them to the screen
        i.move() #increases the x and y coordinates of each bullet object

        if i.hit(target) != None: #collision using mask by passing in what i want to detect colliding with then resets enemy position
            gun_bullets.remove(i) #when bullet hits target stop drawing bullet
            target.target_health -= arsenal[selected_gun]["damage"] #subtracts targets health by current guns damage
            # print(target.target_health)

            if target.target_health <= 0: #when target health reaches 0 target is now dead
                lvl.increase_score() #increments the player score on successful target kills
                death = OOP.Death(selected_target,target.x_pos+target.image.get_width()/2, target.y_pos+target.image.get_height()/2) #creates death animation class for target by passing in targer coordinates
                death_group.add(death) 

                for t in target_group: #stops drawing all target animations
                    t.kill()
                selected_target = random.choice(sprites)
                target = OOP.Target(random.randrange(0,width-100),random.randrange(0,height-100),target_image,target_health,selected_target) #creates a new target object for player to shoot
                target_group.add(target)

    for i in lvl.powerup_lst:
        # print(i.y_pos)
        i.y_pos += gravity #increases the items gravity
        if i.y_pos > height: #if items are greater than the screens height resets their y position
            i.y_pos = random.randrange(-10000,0)

        if i.hit(player) != None:
            print(i.name)

            if i.name == "damage_bonus": #increases guns damage
                print("Increasing guns damage")
                arsenal[selected_gun]["damage"] *= 2

            if i.name == "nuke": #destroys all enemies and targets on screen
                print("BO3 Zombies")
                for enemy in lvl.enemy_lst:
                    if enemy.y_pos>=0 and enemy.y_pos<height: 
                        lvl.enemy_lst.remove(enemy)

                # for enemy in lvl.enemy_lst:
                if target.y_pos>=0 and target.y_pos<height:
                    lvl.increase_score() #increments the player score on successful target kills
                    death = OOP.Death(selected_target,target.x_pos+target.image.get_width()/2, target.y_pos+target.image.get_height()/2) #creates death animation class for target by passing in targer coordinates
                    death_group.add(death) 

                    for t in target_group: #stops drawing all target animations
                        t.kill()
                    selected_target = random.choice(sprites)
                    target = OOP.Target(random.randrange(0,width-100),random.randrange(0,height-100),target_image,target_health,selected_target) #creates a new target object for player to shoot
                    target_group.add(target)

            if i.name == "player_speed_debuff": #slows player movement speed
                print("decreasing player speed")
                if velocity > 1: #sets the lowest speed to 1 if debuff decreases to 0 as a safety net
                    velocity -= 3
                if velocity == 0:
                    velocity = 1

            if i.name == "player_health_bonus": #increases player lives
                print("Increasing player health")
                player.lives += 1

            lvl.powerup_lst.remove(i) #removes item from powerup list
            if len(lvl.powerup_lst) <= 0: #if no mo items are in powerup list generate more items
                lvl.draw_powerup()


    for i in lvl.enemy_lst:
        # print(i.y_pos)
        i.y_pos += gravity #increases the enemys gravity
        if i.y_pos > height: #if enemies are greater than the screens height resets their y position
            i.y_pos = random.randrange(-10000,0)
         
        if i.hit(player) != None: #collision using mask by passing in what i want to detect colliding with
            player.lives -= 1 #subtracts player health by 1 everytim a asteroid hits a player
            lvl.enemy_lst.remove(i) #when enemy hits player stop drawing enemy

            if player.lives <= 0: #when player is out of lives activates death animation for selected player object
                death = OOP.Death(selected_player,player.x_pos+player.image.get_width()/2, player.y_pos+player.image.get_height()/2) #creates death animation class for target by passing in targer coordinates
                death_group.add(death)

                for player_individual in player_group: #removes the sprite from the group
                    player_individual.kill()

                lvl.playing = lvl.lose_level() #ends the game loop
                print("You died")
                arsenal[selected_gun]["loadout"].clear() #if game loop is still running and player dies this removes the guns from the loadout

    gun_offset = 0 #needed to make spacing for guns
    for gun in arsenal[selected_gun]["loadout"]: #cycles through the loadout and draws the guns first iteration draws the gun in the top left corner because the offset is 0 the 2nd iteration is in the top right corner becuase the offset is redeclared to be the player image width
        gun.x_pos = player.x_pos + gun_offset 
        gun.y_pos = player.y_pos 
        gun_offset = player.image.get_width() #redeclares the offset to be the player image top right
    

    # win.fill(black)
    win.blit(bg,(0,0))
    #text has to be placed here before drawing anything else so everything else is drawn in front of it
    win.blit(lvl.score_text,(0,0))
    time_text = pygame.font.Font('freesansbold.ttf', 250).render(lvl.time_str, True, grey)
    win.blit(time_text, (width//2-time_text.get_width()//2,height//2-time_text.get_height()//2)) #draws timer to window and centers in middle of window

    health_offset = 10 #creates a initial health image offset for spacing between the image and the right side of the screen
    for i in range(player.lives): #draws player hearts in top right corner 
        win.blit(health_image,(width-health_image.get_width() - health_offset,10))
        health_offset += health_image.get_width() + 5 #gives the heart images spacing for better visual

    for g in arsenal[selected_gun]["loadout"]: #draws the selected loadout
        g.draw(win)
    # player.draw(win) 
    for p in player_group: #draws player sprite
        p.draw(win) #draws all of the death animations in sprite group 
        p.update()
    for b in gun_bullets: #draws bullets
        b.draw(win)
    # target.draw(win) #
    for t in target_group: #draws target to hit
        t.draw(win)
        t.update()
    for e in lvl.enemy_lst: #draws enemies
        e.draw(win)
    for item in lvl.powerup_lst: #draws items
        item.draw(win)

    death_group.draw(win) #draws all of the death animations in sprite group 
    death_group.update()
    pygame.display.update()
    

pygame.quit()