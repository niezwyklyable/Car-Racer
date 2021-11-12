from .car import Car

class AICar(Car):
    #STATES = 32 # in the future?

    def __init__(self, x, y, lvl):
        super().__init__(x=x, y=y, lvl=lvl)
        self.type = 'AI car'
