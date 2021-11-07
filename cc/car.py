from .sprite import Sprite
from .constants import RED_CAR, GREEN_CAR, PURPLE_CAR, WHITE_CAR, GREY_CAR
import random
from pygame.transform import rotate

class Car(Sprite):
    MAX_SPEED = 3 # this can be changed in the future when levels will be created
    ACCEL = 0.05 # acceleration of a car (realistic feature)
    STATES = 12 # number of possible dirs

    def __init__(self, x, y):
        super().__init__(IMG=None, type='car', x=x, y=y)
        self.pick_random_color()
        self.speed = 0 # from 0 to MAX_SPEED but negative values are also taken into consideration in the future
        self.dir = 0 # there are as many different dirs as STATES says

    def pick_random_color(self):
        self.IMG = random.choice((RED_CAR, GREEN_CAR, PURPLE_CAR, WHITE_CAR, GREY_CAR))
        self.IMGs = {}
        for i in range(self.STATES):
            # rotate() and other transform methods should be used once (means only on an original one) otherwise it's strive for a bugg
            self.IMGs.update({i: rotate(self.IMG, int(-1 * i / self.STATES * 360))})

    def move_forward(self):
        # the car strive for its max speed
        if self.speed < self.MAX_SPEED:
            self.speed += self.ACCEL
        
        # max speed assertion - speed limiter
        if self.speed > self.MAX_SPEED:
            self.speed = self.MAX_SPEED

        if self.dir == 0:
            self.y -= self.speed

        # next time add remaining dirs...

    def turn_left(self):
        if self.dir == 0:
            self.dir = self.STATES - 1
        else:
            self.dir -= 1 
            
        self.IMG = self.IMGs[self.dir]

    def turn_right(self):
        if self.dir == self.STATES - 1:
            self.dir = 0
        else:
            self.dir += 1 
            
        self.IMG = self.IMGs[self.dir]
