import pygame 
from pygame.locals import *
from car import Car
from enemyCar import EnemyCar
from road import Road
# from collision import Collision

class MainGame():
    window = None
    width =  1000
    height = 500
    my_car = Car(800, 230, "images/player.png", width, height, 4)
    background = Road("images/road.png")
    enemyCars = EnemyCar(width)
    # collision = Collision()

    def __init__(self):
        pass

    def getEvent(self):
        eventList = pygame.event.get() # Get all the events from pygame 
        for event in eventList:
            if event.type == pygame.QUIT:
                self.endGame()
            if event.type == pygame.KEYDOWN:
                MainGame.my_car.move()

    def startGame(self):
        # Load the game window
        pygame.display.init() #初始化窗口
        MainGame.window = pygame.display.set_mode([MainGame.width, MainGame.height]) # Set the window size
        pygame.display.set_caption("Racing Game") # Set the window caption
        while True:
            self.getEvent() # Get the event from the getEvent class
            MainGame.background.displayRoad(MainGame.window, MainGame.width, MainGame.height)
            MainGame.enemyCars.draw(MainGame.window)
            MainGame.enemyCars.move()
            MainGame.my_car.displayCar(MainGame.window) # Display the car
            MainGame.my_car.move() # Call the move method from Car class
            # MainGame.collision.collision(MainGame.window)
            pygame.display.update()
            
        
    def endGame(self):
        exit()