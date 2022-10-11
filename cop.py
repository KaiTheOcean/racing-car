import pygame 
import sys 

class Cop:

    def __init__(self):
        self.image = pygame.image.load("images/cop.png")
        self.rect = self.image.get_rect(top=100, bottom=150, left=600, right=650)

    def move(self): 
        self.rect = self.rect.move(-1, 0)
    