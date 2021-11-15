import pytest
from cc.game import Game
from cc.car import Car
from cc.constants import WIDTH, HEIGHT
import pygame

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()

def test_level_from_1_to_2():
    game = Game(WIN)
    game.create_cars()
    game.car.distance = game.car.DISTANCE_THRESHOLD + 1
    if not game.gameover:
        game.update() # finish flag collision
        assert game.level == 2

def test_level_from_2_to_3():
    game = Game(WIN)
    game.level = 2
    game.create_cars()
    game.car.distance = game.car.DISTANCE_THRESHOLD + 1
    if not game.gameover:
        game.update() # finish flag collision
        assert game.level == 3

def test_level_from_3_to_finish():
    game = Game(WIN)
    game.level = 3
    game.create_cars()
    game.car.distance = game.car.DISTANCE_THRESHOLD + 1
    if not game.gameover:
        game.update() # finish flag collision
        assert game.gameover == True
