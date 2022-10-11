import pygame 
import sys 

class Cop(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/cop.png")
        self.rect = self.image.get_rect(top=100, bottom=150, left=600, right=650)

    def move(self): 
        self.rect.move_ip(1, 0)

    