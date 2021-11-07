import pygame
from .finish import FinishFlag
from .constants import BACKGROUND, TRACK, FF_POS_X, FF_POS_Y, RED_CAR
from .car import Car

class Game():
    def __init__(self, win):
        self.win = win
        self.finish_flag = None
        self.car = None
        #self.AI_car = None # in the future...
        self.create_finish_flag(FF_POS_X, FF_POS_Y)
        self.create_cars()

    def render(self):
        self.win.blit(BACKGROUND, (0, 0))
        self.win.blit(TRACK, (0, 0))
        self.finish_flag.draw(self.win)
        self.car.draw(self.win)

        pygame.display.update()

    def update(self):
        self.car.move_forward()

    def create_finish_flag(self, x, y):
        self.finish_flag = FinishFlag(x, y)

    # create a car exactly where the finish flag is (not necessarily on FF_POS_X and FF_POS_Y poses)
    def create_cars(self):
        self.car = Car(self.finish_flag.x-self.finish_flag.IMG.get_width()//4,\
             self.finish_flag.y-self.finish_flag.IMG.get_height()//2+RED_CAR.get_height()//2)

        # AI car in the future... AICar(Car)
        #self.AI_car = AICar(self.finish_flag.x+self.finish_flag.IMG.get_width()//4,\
             #self.finish_flag.y-self.finish_flag.IMG.get_height()//2+RED_CAR.get_height()//2)
