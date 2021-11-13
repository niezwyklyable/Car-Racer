import pygame
from .finish import FinishFlag
from .constants import BACKGROUND, HEIGHT, TRACK, FF_POS_X, FF_POS_Y, RED_CAR, WIDTH, MAX_LEVEL, WHITE, FPS, BLACK
from .car import Car
from .border import TrackBorder
from .AIcar import AICar
from .constants import FINISH_FLAG_REWARD, BORDER_HIT_PENALTY, MOVE_PENALTY # q learning stuff

class Game():
    def __init__(self, win):
        self.win = win
        self.finish_flag = None
        self.finish_flag_grp_obj = None # needed for collision detection
        self.car = None
        self.track_border = None
        self.AI_car = None
        self.create_finish_flag(FF_POS_X, FF_POS_Y)
        self.level = 1
        self.create_cars()
        self.create_border(WIDTH//2, HEIGHT//2)
        self.frames = 0
        self.gameover = False
        self.msg = '' # text that will be blitted in the end of a game
        self.reward = 0 # q learning stuff

    def render(self):
        self.win.blit(BACKGROUND, (0, 0))
        self.win.blit(TRACK, (0, 0))
        self.track_border.draw(self.win) # it is different draw method - comes from Group class
        self.finish_flag.draw(self.win)
        self.AI_car.draw(self.win)
        self.car.draw(self.win)
        self.show_info()

        if self.gameover:
            self.win.blit(self.msg, (int(WIDTH / 2 - self.msg.get_width() / 2), \
                int(HEIGHT / 2 - self.msg.get_height() / 2)))

        pygame.display.update()

    def update(self):
        self.car.move_forward()
        self.AI_car.move_forward()
        self.check_collision()
        self.frames += 1

    def create_finish_flag(self, x, y):
        self.finish_flag = FinishFlag(x, y)
        self.finish_flag_grp_obj = pygame.sprite.Group(self.finish_flag)

    # create a car exactly where the finish flag is (not necessarily on FF_POS_X and FF_POS_Y poses)
    def create_cars(self):
        self.car = Car(self.finish_flag.x-self.finish_flag.image.get_width()//4,\
             self.finish_flag.y-self.finish_flag.image.get_height()//2+RED_CAR.get_height()//2,\
             self.level)

        self.AI_car = AICar(self.finish_flag.x+self.finish_flag.image.get_width()//4,\
             self.finish_flag.y-self.finish_flag.image.get_height()//2+RED_CAR.get_height()//2,\
             self.level)

    def create_border(self, x, y):
        self.track_border = pygame.sprite.Group(TrackBorder(x, y)) # Group class is needed to collision detection

    def check_collision(self):
        # update mask and rect status - it makes sense only for dynamic objects 
        self.car.create_mask()
        self.AI_car.create_mask()

        # if there is no collision with AI car, determines appropriate reward
        self.reward = -MOVE_PENALTY # q learning stuff
 
        # collision detection between car and finish flag (must be as the first checking)
        if pygame.sprite.spritecollide(self.car, self.finish_flag_grp_obj, False, pygame.sprite.collide_mask):
            if self.car.distance > self.car.DISTANCE_THRESHOLD and self.level < MAX_LEVEL:
                self.level += 1
                self.frames = 0
                self.create_cars()
            elif self.car.distance > self.car.DISTANCE_THRESHOLD and self.level >= MAX_LEVEL:
                self.gameover = True
                font = pygame.font.SysFont('comicsans', 80)
                self.msg = font.render('YOU WON!', 1, WHITE, BLACK) # that's quite interesting that the last argument is neither required arg nor kwarg...

        # collision detection between AI car and finish flag
        if pygame.sprite.spritecollide(self.AI_car, self.finish_flag_grp_obj, False, pygame.sprite.collide_mask):
            if self.AI_car.distance > self.AI_car.DISTANCE_THRESHOLD:
                self.reward = FINISH_FLAG_REWARD # q learning stuff
                self.gameover = True
                font = pygame.font.SysFont('comicsans', 80)
                self.msg = font.render('YOU LOST!', 1, WHITE, BLACK)

        # collision detection between car and track border
        # args: Sprite, Group, dokill, collision detection method
        if pygame.sprite.spritecollide(self.car, self.track_border, False, pygame.sprite.collide_mask):
            self.reward = -BORDER_HIT_PENALTY # q learning stuff

            if self.car.speed == self.car.MAX_SPEED:
                self.car.move_backward() # the first bounce is full and independent (without decay)
            elif self.car.is_bouncing:
                self.car.strive_for_stop() # every next bounce is weaker due to speed decay until its reach speed 0
            else:
                self.car.move_backward() # try to restore on the track after bouncing (repeat the process actually)

        # collision detection between AI car and track border
        if pygame.sprite.spritecollide(self.AI_car, self.track_border, False, pygame.sprite.collide_mask):
            if self.AI_car.speed == self.AI_car.MAX_SPEED:
                self.AI_car.move_backward() # the first bounce is full and independent (without decay)
            elif self.AI_car.is_bouncing:
                self.AI_car.strive_for_stop() # every next bounce is weaker due to speed decay until its reach speed 0
            else:
                self.AI_car.move_backward() # try to restore on the track after bouncing (repeat the process actually)

    def show_info(self):
        font = pygame.font.SysFont('comicsans', 30)

        text = font.render(f'Level {self.level}', 1, WHITE)
        self.win.blit(text, (20, 675))

        text = font.render('Speed: {:.0f}px/s'.format(self.car.speed * FPS), 1, WHITE) # px/frame * frames/s
        self.win.blit(text, (20, 705))

        text = font.render(f'Distance: {self.car.distance}frames', 1, WHITE)
        self.win.blit(text, (20, 735))

        text = font.render(f'Time: {int(self.frames / FPS)}s', 1, WHITE) # frames / (frames * s)
        self.win.blit(text, (20, 765))
