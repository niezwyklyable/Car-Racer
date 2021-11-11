from .sprite import MySprite
from .constants import RED_CAR, GREEN_CAR, PURPLE_CAR, WHITE_CAR, GREY_CAR
import random
from pygame.transform import rotate
import math

class Car(MySprite):
    MAX_SPEED = 3 # this can be changed in the future when levels will be created
    ACCEL = 0.05 # acceleration of a car (realistic feature)
    STATES = 16 # number of possible dirs

    def __init__(self, x, y):
        super().__init__(image=None, type='car', x=x, y=y)
        self.speed = 0 # from 0 to MAX_SPEED but negative values are also taken into consideration in the future
        self.dir = 0 # there are as many different dirs as STATES says
        self.pick_random_color()
        self.create_mask()

    def pick_random_color(self):
        random_color = random.choice((RED_CAR, GREEN_CAR, PURPLE_CAR, WHITE_CAR, GREY_CAR))
        self.IMGs = {}
        for i in range(self.STATES):
            # rotate() and other transform methods should be used once (means only on an original one) otherwise it's strive for a bugg
            self.IMGs.update({i: rotate(random_color, int(-1 * i / self.STATES * 360))})

        self.image = self.IMGs[self.dir]

    def move_forward(self):
        # for testing purposes only
        speed_x = 0
        speed_y = self.speed

        # the car strive for its max speed
        if self.speed < self.MAX_SPEED:
            self.speed += self.ACCEL
        
        # max speed assertion - speed limiter
        if self.speed > self.MAX_SPEED:
            self.speed = self.MAX_SPEED

        # move depending on the current direction
        if self.dir == 0:
            self.y -= self.speed
        elif self.dir == self.STATES // 4:
            self.x += self.speed
        elif self.dir == self.STATES // 2:
            self.y += self.speed
        elif self.dir == 3 * self.STATES // 4:
            self.x -= self.speed
        else:
            alfa = float(self.dir / self.STATES * 2 * math.pi)

            if 0 < self.dir < self.STATES // 4:
                sign_x = 1
                sign_y = -1
            elif self.STATES // 4 < self.dir < self.STATES // 2:
                sign_x = 1
                sign_y = 1
            elif self.STATES // 2 < self.dir < 3 * self.STATES // 4:
                sign_x = -1
                sign_y = 1
            else:
                sign_x = -1
                sign_y = -1

            speed_x = sign_x * abs(math.sin(alfa) * self.speed)
            speed_y = sign_y * abs(math.cos(alfa) * self.speed)
            self.x += speed_x
            self.y += speed_y

        # for testing purposes only
        return speed_x, speed_y

    def turn_left(self):
        if self.dir == 0:
            self.dir = self.STATES - 1
        else:
            self.dir -= 1 
            
        self.image = self.IMGs[self.dir]

    def turn_right(self):
        if self.dir == self.STATES - 1:
            self.dir = 0
        else:
            self.dir += 1 
            
        self.image = self.IMGs[self.dir]
