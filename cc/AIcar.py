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
