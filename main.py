import pygame
from gun import Gun
from player import Player
import math

pygame.init()
width,height = 700,700
win = pygame.display.set_mode((width,height))
pygame.display.set_caption("Shooter")
fps = 60
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
blue = (0,0,255)
green = (0,255,0)
playing = True
vel = 10
rocket = pygame.image.load(r"gun-pack\2 Guns\10_1.png")
player_right = pygame.image.load(r"ghost-pack\PNG\Wraith_03\PNG Sequences\Idle\Wraith_03_Idle_000_right.png")
player_left = pygame.image.load(r"ghost-pack\PNG\Wraith_03\PNG Sequences\Idle\Wraith_03_Idle_000_left.png")
player = Player(300,300,player_right,3)
player_img_copy = player.image.copy()
rocket = Gun(player.x_pos,player.y_pos,rocket,1,player)
clock = pygame.time.Clock()

while playing:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            break

    # print(rocket.x_pos,player.x_pos)
    rocket.x_pos = player.x_pos + 80 #puts the gun in top right hovering above player sprite
    rocket.y_pos = player.y_pos 

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player.x_pos += vel
        player.image = pygame.transform.scale(player_right,(100,100)) #changes the orientation of the image to the right


    if keys[pygame.K_a]:
        player.x_pos -= vel
        player.image = pygame.transform.scale(player_left,(100,100)) #changes the orientation of the image to the left



    if keys[pygame.K_w]:
        player.y_pos -= vel
    if keys[pygame.K_s]:
        player.y_pos += vel

    win.fill(black)
    rocket.draw(win)
    player.draw(win)
    pygame.display.update()


pygame.quit()