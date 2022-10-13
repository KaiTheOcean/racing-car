import pygame 
from pygame.locals import *
from car import Car 
from enemyCar import EnemyCar

class Collision():
    text_color = (255,192,203)
    text_position = (400, 200)
    text_color = (255,192,203)
    text_position = (400, 200)
    def __init__(self):
        pass

    def getTextSurface(self, text):
        pygame.font.init()
        font = pygame.font.SysFont("georiga", 30)
        textSurface = font.render(text, True, Collision.text_color)
        return textSurface

    def collision(self, window):
         collide = pygame.Rect.colliderect(Car.rect, EnemyCar.rect1)
         if collide:
            window.blit(self.getTextSurface("Let's speed up!!"), Collision.text_position)
        # my_car = Car(800, 230, "images/player.png", width, height, 4)
        # enemyCars = EnemyCar(width)
        # if my_car.rect == enemyCars.rect1 or my_car.rect == enemyCars.rect2 or my_car.rect == enemyCars.rect3 or my_car.rect == enemyCars.rect4 or my_car.rect == enemyCars.rect5:
        #     window.blit(self.getTextSurface("Let's speed up!!"), Collision.text_position)
        #     return False
            
            
