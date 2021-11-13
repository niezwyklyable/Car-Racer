from .car import Car

class AICar(Car):
    #STATES = 32 # in the future?

    def __init__(self, x, y, lvl):
        super().__init__(x=x, y=y, lvl=lvl)
        self.type = 'AI car'

    # q table interpreter
    def action(self, choice):
        if choice == 0:
            self.turn_left()
        elif choice == 1:
            pass # do nothing (only move_forward() method is called)
        elif choice == 2: # actually else
            self.turn_right()
