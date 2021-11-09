from pygame import sprite
from pygame.mask import from_surface
from .constants import TRACK_BORDER

class TrackBorder(sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = TRACK_BORDER
        self.rect = self.image.get_rect(center=(x, y))
        self.type = 'track border'
        self.x = x
        self.y = y
        self.mask = from_surface(self.image)
