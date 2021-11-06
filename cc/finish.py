from .sprite import Sprite
from .constants import FINISH_FLAG

class FinishFlag(Sprite):
    def __init__(self, x, y):
        super().__init__(IMG=FINISH_FLAG, type='finish flag', x=x, y=y)
