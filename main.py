import pygame
from constants import *
import OOP

pygame.init()
pygame.display.set_caption("Shooter")

while playing:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            break

        if event.type == pygame.KEYDOWN: #detects any keyboard key presses
            if event.key == pygame .K_SPACE: #if spacebar is pressed shoots a bullet
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
            death = OOP.Death(selected_enemy,target.x_pos+target.image.get_width()/2, target.y_pos+target.image.get_height()/2) #creates death animation class for target by passing in targer coordinates
            death_group.add(death)
            target.x_pos = random.randrange(0,width-target.image.get_width()) #resets targets x position to random coordinate within the window width
            target.y_pos = random.randrange(0,height-target.image.get_height()) #resets targets y position to random coordinate within the window height

    for i in enemy_lst:
        i.y_pos += gravity #increases the enemys gravity
        if i.y_pos > height: #if enemies are off screen resets their y position
            i.y_pos = random.randrange(-10000,0)
        
        if i.hit(player): #collision using mask by passing in what i want to detect colliding with 
            enemy_lst.remove(i) #when enemy hits player stop drawing enemy
            death = OOP.Death(selected_player,player.x_pos+player.image.get_width()/2, player.y_pos+player.image.get_height()/2) #creates death animation class for target by passing in targer coordinates
            death_group.add(death)

            for player_individual in player_group: #removes the sprite from the group
                player_individual.kill()

            #moves the players x and y coords off screen
            player.x_pos = -1000 
            player.y_pos = -1000

            ##TODO
            #make a method in level class to stop the game and give option to restart


    arsenal[selected_gun]["loadout"][0].x_pos = player.x_pos + 80 #puts the gun in top right hovering above player sprite
    arsenal[selected_gun]["loadout"][0].y_pos = player.y_pos 

    arsenal[selected_gun]["loadout"][1].x_pos = player.x_pos  #puts the gun in top right hovering above player sprite
    arsenal[selected_gun]["loadout"][1].y_pos = player.y_pos 
    

    win.fill(black)
    for i in arsenal[selected_gun]["loadout"]: #draws the selected loadout
        i.draw(win)
    # player.draw(win) 
    for i in player_group: #draws player sprite
        i.draw(win) #draws all of the death animations in sprite group 
        i.update()
    for b in gun_bullets: #draws bullets
        b.draw(win)
    # target.draw(win) #
    for i in target_group: #draws target to hit
        i.draw(win)
        i.update()
    for e in enemy_lst: #draws enemies
        e.draw(win)

    death_group.draw(win) #draws all of the death animations in sprite group 
    death_group.update()

    pygame.display.update()
    

pygame.quit()