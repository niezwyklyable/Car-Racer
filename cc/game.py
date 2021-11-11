import pygame
from .finish import FinishFlag
from .constants import BACKGROUND, HEIGHT, TRACK, FF_POS_X, FF_POS_Y, RED_CAR, WIDTH, MAX_LEVEL
from .car import Car
from .border import TrackBorder

class Game():
    def __init__(self, win):
        self.win = win
        self.finish_flag = None
        self.finish_flag_grp_obj = None # needed for collision detection
        self.car = None
        self.track_border = None
        #self.AI_car = None # in the future...
        self.create_finish_flag(FF_POS_X, FF_POS_Y)
        self.level = 2
        self.create_cars()
        self.create_border(WIDTH//2, HEIGHT//2)

    def render(self):
        self.win.blit(BACKGROUND, (0, 0))
        self.win.blit(TRACK, (0, 0))
        self.track_border.draw(self.win) # it is different draw method - comes from Group class
        self.finish_flag.draw(self.win)
        self.car.draw(self.win)

        pygame.display.update()

    def update(self):
        self.car.move_forward()
        self.check_collision()

    def create_finish_flag(self, x, y):
        self.finish_flag = FinishFlag(x, y)
        self.finish_flag_grp_obj = pygame.sprite.Group(self.finish_flag)

    # create a car exactly where the finish flag is (not necessarily on FF_POS_X and FF_POS_Y poses)
    def create_cars(self):
        self.car = Car(self.finish_flag.x-self.finish_flag.image.get_width()//4,\
             self.finish_flag.y-self.finish_flag.image.get_height()//2+RED_CAR.get_height()//2,\
             self.level)

        # AI car in the future... AICar(Car)
        #self.AI_car = AICar(self.finish_flag.x+self.finish_flag.image.get_width()//4,\
             #self.finish_flag.y-self.finish_flag.image.get_height()//2+RED_CAR.get_height()//2)

    def create_border(self, x, y):
        self.track_border = pygame.sprite.Group(TrackBorder(x, y)) # Group class is needed to collision detection

    def check_collision(self):
        # update mask and rect status - it makes sense only for dynamic objects 
        self.car.create_mask()
 
        # collision detection between car and finish flag (must be as the first checking)
        if pygame.sprite.spritecollide(self.car, self.finish_flag_grp_obj, False, pygame.sprite.collide_mask):
            if self.car.distance > self.car.DISTANCE_THRESHOLD and self.level < MAX_LEVEL:
                self.level += 1
                self.create_cars()
            elif self.car.distance > self.car.DISTANCE_THRESHOLD and self.level >= MAX_LEVEL:
                self.end_of_game()

        # collision detection between car and track border
        # args: Sprite, Group, dokill, collision detection method
        if pygame.sprite.spritecollide(self.car, self.track_border, False, pygame.sprite.collide_mask):
            if self.car.speed == self.car.MAX_SPEED:
                self.car.move_backward() # the first bounce is full and independent (without decay)
            elif self.car.is_bouncing:
                self.car.strive_for_stop() # every next bounce is weaker due to speed decay until its reach speed 0
            else:
                self.car.move_backward() # try to restore on the track after bouncing (repeat the process actually)

    def end_of_game(self):
        print('END OF THE GAME! YOU REACHED MAX LEVEL!')
