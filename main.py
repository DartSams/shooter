import pygame
from constants import *
from level import Level
from death import Death

pygame.init()
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Shooter")

while playing:
    clock.tick(fps)
    for i in gun_bullets: #when there are bullets in the list draws them to the screen
        i.move() 
        rect = i.image.get_rect()
        if i.hit(target): #collision using mask by passing in what i want to detect colliding with then resets enemy position
            death = Death(target.x_pos+target.image.get_width()/2, target.y_pos+target.image.get_height()/2) #creates death animation class for target by passing in targer coordinates
            death_group.add(death)
            target.x_pos = random.randrange(0,width-target.image.get_width()) #resets targets x position to random coordinate within the window width
            target.y_pos = random.randrange(0,height-target.image.get_height()) #resets targets y position to random coordinate within the window height

    for i in enemy_lst:
        i.y_pos += gravity #increases the enemys gravity
        if i.y_pos > height: #if enemies are off screen resets their y position
            i.y_pos = random.randrange(-10000,0)
        
        if i.hit(player): #collision using mask by passing in what i want to detect colliding with then resets enemy position
            enemy_lst.remove(i) #when enemy hits player stop drawing enemy
            death = Death(player.x_pos+player.image.get_width()/2, player.y_pos+player.image.get_height()/2) #creates death animation class for target by passing in targer coordinates
            death_group.add(death)
            ##TODO
            #make function to stop drawing player on player death

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame .K_SPACE: #if spacebar is pressed shoots a bullet
                for i in loadout:
                    i.shoot(gun_bullets)



    loadout[0].x_pos = player.x_pos + 80 #puts the gun in top right hovering above player sprite
    loadout[0].y_pos = player.y_pos 

    loadout[1].x_pos = player.x_pos  #puts the gun in top right hovering above player sprite
    loadout[1].y_pos = player.y_pos 

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
    


    win.fill(black)
    for i in loadout: #draws the selected loadout
        i.draw(win)
    player.draw(win) #draws player sprite
    for b in gun_bullets: #draws bullets
        b.draw(win)
    target.draw(win) #draws target to hit
    for e in enemy_lst: #draws enemies
        e.draw(win)

    death_group.draw(win) #draws all of the death animations in sprite group 
    death_group.update()

    pygame.display.update()
    

pygame.quit()