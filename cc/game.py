import pygame
from .constants import BACKGROUND

# testing purposes only
from .sprite import Sprite
from .constants import TRACK, TRACK_BORDER, FINISH_FLAG, GREEN_CAR, GREY_CAR, \
     PURPLE_CAR, RED_CAR, WHITE_CAR
from .maths import WIDTH, HEIGHT

class Game():
    def __init__(self, win):
        self.win = win
        self.create_objects()

    def render(self):
        self.win.blit(BACKGROUND, (0, 0))
        
        # testing purposes only
        for to in self.test_objects:
            to.draw(self.win)

        pygame.display.update()

    def update(self):
        pass

    # testing purposes only
    def create_objects(self):
        self.test_objects = []
        #self.test_objects.append(Sprite(TRACK, WIDTH // 2, HEIGHT // 2))
        self.test_objects.append(Sprite(TRACK_BORDER, WIDTH // 2, HEIGHT // 2))
        self.test_objects.append(Sprite(WHITE_CAR, 0, 0))
        self.test_objects.append(Sprite(GREEN_CAR, 100, 100))
        self.test_objects.append(Sprite(RED_CAR, 200, 200))
        self.test_objects.append(Sprite(GREY_CAR, 300, 300))
        self.test_objects.append(Sprite(PURPLE_CAR, 400, 400))
        self.test_objects.append(Sprite(FINISH_FLAG, 500, 500))
