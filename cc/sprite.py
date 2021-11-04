# this is an abstract class - instantiating for testing purposes only !!!
class Sprite():
    def __init__(self, IMG, x=0, y=0, type='abstract_sprite'):
        self.IMG = IMG
        self.x = x
        self.y = y
        self.type = type

    def draw(self, win):
        win.blit(self.IMG, (self.x - self.IMG.get_width() // 2, \
            self.y - self.IMG.get_height() // 2))

    def move(self):
        pass
