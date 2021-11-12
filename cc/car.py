from .sprite import MySprite
from .constants import RED_CAR, GREEN_CAR, PURPLE_CAR, WHITE_CAR, GREY_CAR
import random
from pygame.transform import rotate
import math

class Car(MySprite):
    STATES = 16 # number of possible dirs
    SPEED_DECAY = 0.8 # coeff of speed decaying when car is collide with track border
    STOP_THRESHOLD = 0.03 # if abs of speed is below it during the bouncing, the car completely and immediately stops

    def __init__(self, x, y, lvl):
        super().__init__(image=None, type='car', x=x, y=y)
        self.speed = 0 # from -MAX_SPEED to MAX_SPEED
        self.dir = 0 # there are as many different dirs as STATES says
        self.pick_random_color()
        self.create_mask()
        self.is_bouncing = True # the flag needed to try the car restores on the track by itself
        self.distance = 0 # distance that the car rode (number of frames)
        self.lvl = lvl
        self.set_parameters() # depending on game lvl

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

        # needed for finish flag collision detection
        self.distance += 1

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

            speed_x = sign_x * abs(math.sin(alfa)) * self.speed
            speed_y = sign_y * abs(math.cos(alfa)) * self.speed
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

    def move_backward(self):
        self.is_bouncing = True
        self.speed = -self.MAX_SPEED

    # thanks to that method the car is not going to loop the multiple collisions
    def strive_for_stop(self):
        if abs(self.speed) > self.STOP_THRESHOLD:
            self.speed *= -self.SPEED_DECAY
        else:
            self.is_bouncing = False
            self.speed = 0

    def set_parameters(self):
        # ACCEL - acceleration of a car (realistic feature)
        # DISTANCE_THRESHOLD - the distance that the car has to rode to be able to collide with the finish flag (measured on the manual tests)
        if self.lvl == 1:
            self.MAX_SPEED = 3
            self.ACCEL = 0.05
            self.DISTANCE_THRESHOLD = 1000
        elif self.lvl == 2:
            self.MAX_SPEED = 4
            self.ACCEL = 0.07
            self.DISTANCE_THRESHOLD = 800
        else:
            self.MAX_SPEED = 5
            self.ACCEL = 0.1
            self.DISTANCE_THRESHOLD = 600
