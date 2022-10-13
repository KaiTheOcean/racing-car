import pygame 
from pygame.locals import *

class Road():
    def __init__(self, image_path):
        self.image_path = image_path
        self.i = 0

    def displayRoad(self, window, width, height):
        image = pygame.image.load(self.image_path)
        image = pygame.transform.scale(image,(width,height))

        # Display the road and make it move
        window.blit(image,(self.i,0))
        window.blit(image,(width+self.i,0))
        if (self.i==-width):
            window.blit(image,(width+self.i,0))
            self.i=0
        self.i-=1        