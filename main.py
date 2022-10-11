import pygame
from pygame.locals import *
import sys
import player
import cop
import collision
import enemy

# Set the pygame window size
pygame.init()
width = 1000
height = 400
screen_window = pygame.display.set_mode((width, height))
bg_color = (0, 0, 0)

# Set the caption name
pygame.display.set_caption("Racing Car")

clock = pygame.time.Clock()
# Set the rectangle
screen_rect = screen_window.get_rect()

# Create player, all other enemy cars
player = player.Player()
cop = cop.Cop()
# background = background.Background()
background_image = pygame.image.load("images/road.png")
background_image = pygame.transform.scale(background_image, (width, height))

# Define enemies sprite group 
enemies = pygame.sprite.Group()
enemies.add(cop)



i = 0
# Run the game
running = True 
while running: 
    screen_window.blit(background_image, (i, 0)) # Display background picture
    screen_window.blit(background_image, (width+i, 0)) # Redisplay the background picture
    if (i == -width):
        screen_window.blit(background_image, (width+i, 0))
        i = 0
    i -= 1
    screen_window.blit(player.image, player.rect) # Display player car
    screen_window.blit(cop.image, cop.rect) # Display cop car
    player.control_player()
    cop.move()
    pygame.display.flip()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False

    if pygame.sprite.spritecollide(player, enemies, False):
        print(11)
    pygame.display.update()