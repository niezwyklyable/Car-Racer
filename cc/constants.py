from pygame.image import load
from pygame.transform import scale
from .maths import scale_x, scale_y, WIDTH, HEIGHT

# finish flag standard position
FF_POS_X, FF_POS_Y = 175, 270

# finish flag target dims
FF_TARGET_W, FF_TARGET_H = 70, 20

# car size reductor
COEF = 0.7

# assets
BACKGROUND = scale(load('imgs/grass.jpg'), (WIDTH, HEIGHT))
TRACK = scale(load('imgs/track.png'), (WIDTH, HEIGHT))
TRACK_BORDER = scale(load('imgs/track-border.png'), (WIDTH, HEIGHT))
FINISH_FLAG = scale(load('imgs/finish.png'), (FF_TARGET_W, FF_TARGET_H))
GREEN_CAR = scale(load('imgs/green-car.png'), (scale_x(38, target=WIDTH*COEF), scale_y(76, target=HEIGHT*COEF)))
GREY_CAR = scale(load('imgs/grey-car.png'), (scale_x(38, target=WIDTH*COEF), scale_y(76, target=HEIGHT*COEF)))
PURPLE_CAR = scale(load('imgs/purple-car.png'), (scale_x(38, target=WIDTH*COEF), scale_y(76, target=HEIGHT*COEF)))
RED_CAR = scale(load('imgs/red-car.png'), (scale_x(38, target=WIDTH*COEF), scale_y(76, target=HEIGHT*COEF)))
WHITE_CAR = scale(load('imgs/white-car.png'), (scale_x(38, target=WIDTH*COEF), scale_y(76, target=HEIGHT*COEF)))
