import pytest
from cc.car import Car
from cc.constants import WIDTH, HEIGHT
import math

def test_speed_level_1():
    car = Car(WIDTH//2, HEIGHT//2, 1)
    car.speed = car.MAX_SPEED

    for i in range(car.STATES):
        car.dir = i
        speed_x, speed_y = car.move_forward()
        assert car.speed == round(math.sqrt(speed_x ** 2 + speed_y ** 2), 0)

def test_speed_level_2():
    car = Car(WIDTH//2, HEIGHT//2, 2)
    car.speed = car.MAX_SPEED

    for i in range(car.STATES):
        car.dir = i
        speed_x, speed_y = car.move_forward()
        assert car.speed == round(math.sqrt(speed_x ** 2 + speed_y ** 2), 0)

def test_speed_level_3():
    car = Car(WIDTH//2, HEIGHT//2, 3)
    car.speed = car.MAX_SPEED

    for i in range(car.STATES):
        car.dir = i
        speed_x, speed_y = car.move_forward()
        assert car.speed == round(math.sqrt(speed_x ** 2 + speed_y ** 2), 0)
        