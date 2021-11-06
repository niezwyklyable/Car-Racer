# this is an abstract class - no instantiating allowed !!!
class Sprite():
    def __init__(self, x=0, y=0, IMG=None, type=''):
        self.x = x
        self.y = y
        self.IMG = IMG
        self.type = type

    def draw(self, win):
        win.blit(self.IMG, (self.x - self.IMG.get_width() // 2, \
            self.y - self.IMG.get_height() // 2))

    def move(self):
        pass
