import pygame 
import sys 
from pygame.locals import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        '''Set the player positoin'''
        super().__init__() #  调用父类__init__方法初始化对象
        self.image = pygame.image.load("images/player.png")
        self.rect = self.image.get_rect(top=120, bottom=230, left=10, right=700)
    
    def move(self):
        '''Move the car by player'''
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -3)
        elif pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 3)
        elif pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        elif pressed_keys[K_RIGHT]:
            self.rect.move_ip(5 ,0)
    
    def gameOver(self):
        black = (0, 0, 0)
        self.red = "#FA8072"
        self.gameOver = ("Game Over", True, black)