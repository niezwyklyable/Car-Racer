from pygame.image import load
from pygame.transform import scale

# screen refreshing frequency
FPS = 30

# screen dims
WIDTH, HEIGHT = 800, 800

# finish flag standard position
FF_POS_X, FF_POS_Y = 175, 270

# finish flag target dims
FF_TARGET_W, FF_TARGET_H = 70, 20

# car original dims
CAR_W, CAR_H = 38, 76

# car size reductor
COEF = 0.6

# max level of a game
MAX_LEVEL = 3

# assets
BACKGROUND = scale(load('imgs/grass.jpg'), (WIDTH, HEIGHT))
TRACK = scale(load('imgs/track.png'), (WIDTH, HEIGHT))
TRACK_BORDER = scale(load('imgs/track-border.png'), (WIDTH, HEIGHT))
FINISH_FLAG = scale(load('imgs/finish.png'), (FF_TARGET_W, FF_TARGET_H))
GREEN_CAR = scale(load('imgs/green-car.png'), (int(CAR_W * COEF), int(CAR_H * COEF)))
GREY_CAR = scale(load('imgs/grey-car.png'), (int(CAR_W * COEF), int(CAR_H * COEF)))
PURPLE_CAR = scale(load('imgs/purple-car.png'), (int(CAR_W * COEF), int(CAR_H * COEF)))
RED_CAR = scale(load('imgs/red-car.png'), (int(CAR_W * COEF), int(CAR_H * COEF)))
WHITE_CAR = scale(load('imgs/white-car.png'), (int(CAR_W * COEF), int(CAR_H * COEF)))

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
