from .sprite import Sprite
from .constants import RED_CAR, GREEN_CAR, PURPLE_CAR, WHITE_CAR, GREY_CAR

class Car(Sprite):
    def __init__(self, IMG, x, y):
        super().__init__(IMG=IMG, type='car', x=x, y=y)

class RedCar(Car):
    def __init__(self, x, y):
        super().__init__(RED_CAR, x, y)

class GreenCar(Car):
    def __init__(self, x, y):
        super().__init__(GREEN_CAR, x, y)

class PurpleCar(Car):
    def __init__(self, x, y):
        super().__init__(PURPLE_CAR, x, y)

class WhiteCar(Car):
    def __init__(self, x, y):
        super().__init__(WHITE_CAR, x, y)

class GreyCar(Car):
    def __init__(self, x, y):
        super().__init__(GREY_CAR, x, y)
