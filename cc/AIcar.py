from .car import Car
from .constants import AI_STATES

class AICar(Car):
    STATES = AI_STATES

    def __init__(self, x, y, lvl):
        super().__init__(x=x, y=y, lvl=lvl)
        self.type = 'AI car'

    # q table interpreter
    def action(self, choice):
        if choice == 0:
            self.turn_left()
        elif choice == 1:
            self.turn_right()
        else:
            pass # do nothing (only move_forward() method is called)

    def set_parameters(self):
        # ACCEL - acceleration of a car (realistic feature)
        # DISTANCE_THRESHOLD - the distance that the car has to rode to be able to collide with the finish flag (measured on the manual tests)
        if self.lvl == 1:
            self.MAX_SPEED = 2
            self.ACCEL = 0.03
            self.DISTANCE_THRESHOLD = 1300
        elif self.lvl == 2:
            self.MAX_SPEED = 3
            self.ACCEL = 0.05
            self.DISTANCE_THRESHOLD = 1000
        else:
            self.MAX_SPEED = 4
            self.ACCEL = 0.07
            self.DISTANCE_THRESHOLD = 800
