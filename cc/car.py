from .sprite import Sprite
from .constants import RED_CAR, GREEN_CAR, PURPLE_CAR, WHITE_CAR, GREY_CAR
import random

class Car(Sprite):
    MAX_SPEED = 3 # this can be changed in the future when levels will be created
    ACCEL = 0.05 # acceleration of a car (realistic feature)

    def __init__(self, x, y):
        super().__init__(IMG=None, type='car', x=x, y=y)
        self.pick_random_color()
        self.speed = 0 # from 0 to MAX_SPEED but negative values are also taken into consideration in the future
        self.dir = 0 # there are 12 different dirs (from 0 to 11)

    def pick_random_color(self):
        self.IMG = random.choice((RED_CAR, GREEN_CAR, PURPLE_CAR, WHITE_CAR, GREY_CAR))

    def move_forward(self):
        # the car strive for its max speed
        if self.speed < self.MAX_SPEED:
            self.speed += self.ACCEL
        
        # max speed assertion - speed limiter
        if self.speed > self.MAX_SPEED:
            self.speed = self.MAX_SPEED

        if self.dir == 0:
            self.y -= self.speed
