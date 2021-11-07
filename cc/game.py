import pygame
from .finish import FinishFlag
from .constants import BACKGROUND, TRACK, FF_POS_X, FF_POS_Y, RED_CAR
from .car import Car

class Game():
    def __init__(self, win):
        self.win = win
        self.finish_flag = None
        self.cars = []
        self.create_finish_flag(FF_POS_X, FF_POS_Y)
        self.create_cars()

    def render(self):
        self.win.blit(BACKGROUND, (0, 0))
        self.win.blit(TRACK, (0, 0))
        self.finish_flag.draw(self.win)

        for c in self.cars:
            c.draw(self.win)

        pygame.display.update()

    def update(self):
        pass

    def create_finish_flag(self, x, y):
        self.finish_flag = FinishFlag(x, y)

    def create_cars(self):
        self.cars.append(Car(self.finish_flag.x-self.finish_flag.IMG.get_width()//4,\
             self.finish_flag.y-self.finish_flag.IMG.get_height()//2+RED_CAR.get_height()//2))

        # AI car in the future... AICar(Car)
        #self.cars.append(AICar(self.finish_flag.x+self.finish_flag.IMG.get_width()//4,\
             #self.finish_flag.y-self.finish_flag.IMG.get_height()//2+RED_CAR.get_height()//2))
