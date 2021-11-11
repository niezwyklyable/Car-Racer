from pygame import sprite
from pygame.mask import from_surface

# this is an abstract class - no instantiating allowed !!!
class MySprite(sprite.Sprite):
    # inheritence from Sprite class is needed to collision detection properly working
    def __init__(self, image, type, x, y):
        super().__init__()
        self.image = image
        self.type = type
        self.x = x
        self.y = y

    def draw(self, win):
         win.blit(self.image, (self.x - self.image.get_width() // 2, \
             self.y - self.image.get_height() // 2))

    def move(self):
        pass

    # needed to collision detection - for static objects one call is enough
    def create_mask(self):
        self.mask = from_surface(self.image) # determines pixel distribution of an image (sth like that)
        self.rect = self.image.get_rect(center=(self.x, self.y)) # determines position of an image in rectangular form (sth like that)
