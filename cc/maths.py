# 900 x 900 - original dims
# target dims
WIDTH = 800
HEIGHT = 800

def scale_x(x):
    return int(x / 900 * WIDTH)

def scale_y(y):
    return int(y / 900 * HEIGHT)
