from .sprite import MySprite
from .constants import TRACK_BORDER

class TrackBorder(MySprite):
    def __init__(self, x, y):
        super().__init__(image=TRACK_BORDER, type='track border', x=x, y=y)
        self.create_mask()
