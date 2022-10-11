import pygame
from pygame import *
import sys
import player
import cop
import background

# Set the pygame window size
pygame.init()
screen_window = pygame.display.set_mode((1000, 400))
bg_color = (0, 0, 0)

# Set the caption name
pygame.display.set_caption("Racing Car")

clock = pygame.time.Clock()
# Set the rectangle
screen_rect = screen_window.get_rect()

# Create player, all other enemy cars
player = player.Player()
cop = cop.Cop()
background = background.Background()

i = 0
# Run the game
running = True 
while running: 
    screen_window.blit(background.image, (0, -50))
    screen_window.blit(player.image, player.rect)
    screen_window.blit(cop.image, cop.rect)
    player.control_player()
    cop.move()
    pygame.display.flip()
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()