from re import T
from tracemalloc import start
import pygame
from constants import *
import OOP

pygame.init()
pygame.display.set_caption("Shooter")
pygame.time.set_timer(pygame.USEREVENT, 1000)

while lvl.playing:
    lvl.clock.tick(lvl.fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lvl.playing = False
            break

        if event.type == pygame.USEREVENT: #decrements the set timer in each level 
            lvl.time -= 1
            lvl.time_str = str(lvl.time) 
            if lvl.time > 0:
                pass
            else: #when timer reaches 0 then 
                lvl.playing = False
            # print(lvl.text)

        if event.type == pygame.KEYDOWN: #detects any keyboard key presses
            if event.key == pygame.K_SPACE: #if spacebar is pressed shoots a bullet
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
        rect = i.image.get_rect()
        if i.hit(target): #collision using mask by passing in what i want to detect colliding with then resets enemy position
            lvl.increase_score() #increments the player score on successful hits on the targets
            death = OOP.Death(selected_enemy,target.x_pos+target.image.get_width()/2, target.y_pos+target.image.get_height()/2) #creates death animation class for target by passing in targer coordinates
            death_group.add(death)
            target.x_pos = random.randrange(0,width-target.image.get_width()) #resets targets x position to random coordinate within the window width
            target.y_pos = random.randrange(0,height-target.image.get_height()) #resets targets y position to random coordinate within the window height

    for i in lvl.enemy_lst:
        # print(i.y_pos)
        i.y_pos += gravity #increases the enemys gravity
        if i.y_pos > height: #if enemies are off screen resets their y position
            i.y_pos = random.randrange(-10000,0)
         
        if i.hit(player) != None: #collision using mask by passing in what i want to detect colliding with 
            playing = False
            lvl.enemy_lst.remove(i) #when enemy hits player stop drawing enemy
            death = OOP.Death(selected_player,player.x_pos+player.image.get_width()/2, player.y_pos+player.image.get_height()/2) #creates death animation class for target by passing in targer coordinates
            death_group.add(death)

            for player_individual in player_group: #removes the sprite from the group
                player_individual.kill()

            #moves the players x and y coords off screen
            player.x_pos = -1000 
            player.y_pos = -1000
            # print(i.hit(player))
            # playing = lvl.lose_level() #ends the game loop

            ##TODO
            #make  a method in level class to stop the game and give option to restart


    arsenal[selected_gun]["loadout"][0].x_pos = player.x_pos + 80 #puts the gun in top right hovering above player sprite
    arsenal[selected_gun]["loadout"][0].y_pos = player.y_pos 

    arsenal[selected_gun]["loadout"][1].x_pos = player.x_pos  #puts the gun in top right hovering above player sprite
    arsenal[selected_gun]["loadout"][1].y_pos = player.y_pos 
    

    win.fill(black)
    #text has to be placed here before drawing anything else so everything else is drawn in front of it
    win.blit(lvl.score_text,(0,0))
    time_text = pygame.font.Font('freesansbold.ttf', 250).render(lvl.time_str, True, (100, 100, 100))
    win.blit(time_text, (width//2-time_text.get_width()//2,height//2-time_text.get_height()//2)) #draws timer to window and centers in middle of window
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

    death_group.draw(win) #draws all of the death animations in sprite group 
    death_group.update()
    pygame.display.update()
    

pygame.quit()