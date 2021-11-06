import pygame
from cc.finish import FinishFlag
from .constants import BACKGROUND, TRACK

class Game():
    def __init__(self, win):
        self.win = win
        self.finish_flag = None
        self.create_finish_flag()

    def render(self):
        self.win.blit(BACKGROUND, (0, 0))
        self.win.blit(TRACK, (0, 0))
        self.finish_flag.draw(self.win)

        pygame.display.update()

    def update(self):
        pass

    def create_finish_flag(self):
        self.finish_flag = FinishFlag(175, 270)
