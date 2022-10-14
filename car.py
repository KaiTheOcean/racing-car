import pygame 
from pygame.locals import *


class Car():
    def __init__(self, left, top, image_path, screen_width, screen_height, speed):
        '''Add the car position'''
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = pygame.image.load(image_path)  # Save loaded images
        self.rect = self.image.get_rect() # Find the image rect position
        self.rect.left = left # Get the left positon 
        self.rect.top = top # Get the top position
        self.speed = speed # Set the Car speed

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            if self.rect.top > 40:
                self.rect.move_ip(0, -self.speed) # Car can't go over the top of the screen
        elif pressed_keys[K_DOWN]:
            if self.rect.top + self.rect.height < self.screen_height-40:
                self.rect.move_ip(0, self.speed)
        elif pressed_keys[K_LEFT]:
            if self.rect.left > 0:
                self.rect.move_ip(-self.speed, 0) # Car can't go over the left of the screen
        elif pressed_keys[K_RIGHT]:
            if self.rect.left + self.rect.height < self.screen_width:
                self.rect.move_ip(self.speed ,0) # Car can't go over the right of the screen
            
    def displayCar(self, window):
        window.blit(self.image, self.rect)