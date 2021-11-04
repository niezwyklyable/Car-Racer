from pygame.image import load
from pygame.transform import scale
from .maths import scale_x, scale_y, WIDTH, HEIGHT

BACKGROUND = scale(load('imgs/grass.jpg'), (WIDTH, HEIGHT))
TRACK = scale(load('imgs/track.png'), (scale_x(900), scale_y(900)))
TRACK_BORDER = scale(load('imgs/track-border.png'), (scale_x(900), scale_y(900)))
FINISH_FLAG = scale(load('imgs/finish.png'), (scale_x(100), scale_y(20)))
GREEN_CAR = scale(load('imgs/green-car.png'), (scale_x(38), scale_y(76)))
GREY_CAR = scale(load('imgs/grey-car.png'), (scale_x(38), scale_y(76)))
PURPLE_CAR = scale(load('imgs/purple-car.png'), (scale_x(38), scale_y(76)))
RED_CAR = scale(load('imgs/red-car.png'), (scale_x(38), scale_y(76)))
WHITE_CAR = scale(load('imgs/white-car.png'), (scale_x(38), scale_y(76)))
