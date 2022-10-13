# In this game, we need 
# car class (plaer's class and enemies cars class)
#   1. player's class is controled by player
#   2. enemies cars just display and loop them
# raod class 
#   1. Load the image 
#   2. Doesn't allow player go over edge
# collision class 
#   1. When enemies cars and players car hit each other
# And maybe mucis clss 
# main class: 
#   1. start game 
#   2. end game

import pygame 
from pygame.locals import *
from mainGame import MainGame

game = MainGame()
game.startGame()