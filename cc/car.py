from .sprite import Sprite
from .constants import RED_CAR, GREEN_CAR, PURPLE_CAR, WHITE_CAR, GREY_CAR
import random

class Car(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG=None, type='car', x=x, y=y)
        self.pick_random_color()

    def pick_random_color(self):
        self.IMG = random.choice((RED_CAR, GREEN_CAR, PURPLE_CAR, WHITE_CAR, GREY_CAR))
