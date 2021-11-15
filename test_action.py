import pytest
from cc.AIcar import AICar
from cc.constants import WIDTH, HEIGHT, AI_STATES

def test_action_turn_left():
    AI_car = AICar(WIDTH//2, HEIGHT//2, 1)
    AI_car.action(0)
    assert AI_car.dir == AI_STATES - 1

def test_action_turn_right():
    AI_car = AICar(WIDTH//2, HEIGHT//2, 1)
    AI_car.action(1)
    assert AI_car.dir == 1
        