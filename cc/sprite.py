from pygame.mask import from_surface

# this is an abstract class - no instantiating allowed !!!
class Sprite():
    def __init__(self, IMG, type, x, y):
        self.IMG = IMG
        self.type = type
        self.x = x
        self.y = y

    def draw(self, win):
        win.blit(self.IMG, (self.x - self.IMG.get_width() // 2, \
            self.y - self.IMG.get_height() // 2))

    def move(self):
        pass

    # needed to collision detection
    def create_mask(self):
        self.mask = from_surface(self.IMG) 
        self.rect = self.IMG.get_rect(center=(self.x, self.y))
