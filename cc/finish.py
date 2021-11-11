from .sprite import MySprite
from .constants import FINISH_FLAG

class FinishFlag(MySprite):
    def __init__(self, x, y):
        super().__init__(image=FINISH_FLAG, type='finish flag', x=x, y=y)
        self.create_mask()
