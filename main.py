import pygame
from constants import *

pygame.init()
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Shooter")

while playing:
    clock.tick(fps)
    for i in gun_bullets: #when there are bullets in the list draws them to the screen
        i.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            break

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                for i in loadout:
                    i.shoot(gun_bullets)

    loadout[0].x_pos = player.x_pos + 80 #puts the gun in top right hovering above player sprite
    loadout[0].y_pos = player.y_pos 

    loadout[1].x_pos = player.x_pos  #puts the gun in top right hovering above player sprite
    loadout[1].y_pos = player.y_pos 

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]: #right
        player.x_pos += velocity
        player.image = pygame.transform.scale(player_right,(100,100)) #changes the orientation of the image to the right

    if keys[pygame.K_a]:#left
        player.x_pos -= velocity
        player.image = pygame.transform.scale(player_left,(100,100)) #changes the orientation of the image to the left

    if keys[pygame.K_w]:#up
        player.y_pos -= velocity
    if keys[pygame.K_s]:#down
        player.y_pos += velocity



    win.fill(black)
    # rocket.draw(win)
    for i in loadout:
        i.draw(win)
    player.draw(win)
    for b in gun_bullets:
        b.draw(win)
    pygame.display.update()


pygame.quit()