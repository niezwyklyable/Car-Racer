import pytest
from cc.car import Car
from cc.maths import WIDTH, HEIGHT
import math

def test_dirs():
    car = Car(WIDTH//2, HEIGHT//2)
    car.speed = car.MAX_SPEED

    for i in range(car.STATES):
        car.dir = i
        speed_x, speed_y = car.move_forward()
        assert car.speed == round(math.sqrt(speed_x ** 2 + speed_y ** 2), 0)
