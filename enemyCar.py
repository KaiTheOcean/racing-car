import pygame 
import random
from pygame.locals import *
import time 

class EnemyCar(pygame.sprite.Sprite):
      def __init__(self, screen_width):
        super().__init__() 
        self.screen_width = screen_width
        self.image1 = pygame.image.load("images/enemy1.png")
        self.image2 = pygame.image.load("images/enemy2.png")
        self.image3 = pygame.image.load("images/enemy3.png")
        self.image4 = pygame.image.load("images/enemy4.png")
        self.image5 = pygame.image.load("images/enemy5.png")
        self.rect1 = self.image1.get_rect()
        self.rect2 = self.image2.get_rect()
        self.rect3 = self.image3.get_rect()
        self.rect4 = self.image4.get_rect()
        self.rect5 = self.image5.get_rect()
        self.rect1.center= (0,random.randint(70,screen_width-70))
        self.rect2.center= (0,random.randint(70,screen_width-70))
        self.rect3.center= (0,random.randint(70,screen_width-70))
        self.rect4.center= (0,random.randint(70,screen_width-70))
        self.rect5.center= (0,random.randint(70,screen_width-70))
 
      def move(self):
        self.rect1.move_ip(1,0)
        self.rect2.move_ip(2,0)
        self.rect3.move_ip(1,0)
        self.rect4.move_ip(5,0)
        self.rect5.move_ip(1,0)
        if (self.rect1.left > 1000):
            self.rect1.left = 0
            self.rect1.center = (0, random.randint(70, 430))
        if (self.rect2.left > 1000):
            self.rect2.left = 0
            self.rect2.center = (0, random.randint(70, 430))
        if (self.rect3.left > 1000):
            self.rect3.left = 0
            self.rect3.center = (0, random.randint(70, 430))
        if (self.rect4.left > 1000):
            self.rect4.left = 0
            self.rect4.center = (0, random.randint(70, 430))
        if (self.rect5.left > 1000):
            self.rect5.left = 0
            self.rect5.center = (0, random.randint(70, 430))
 
      def draw(self, window):
        window.blit(self.image1, self.rect1) 
        window.blit(self.image1, self.rect1) 
        window.blit(self.image2, self.rect2) 
        window.blit(self.image3, self.rect3) 
        window.blit(self.image4, self.rect4)
        window.blit(self.image5, self.rect5)  


