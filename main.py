import pygame
from cc.constants import WIDTH, HEIGHT, FPS, WHITE, BLACK, SHOW_EVERY, EPISODES, TRAINED_LEVEL, ORANGE, GREEN
from cc.game import Game

# q learning stuff
import numpy as np
import pickle
from cc.constants import CHOICES, FINISH_FLAG_REWARD, BORDER_HIT_PENALTY, EPS_START, EPS_DECAY, LEARNING_RATE, DISCOUNT, EPISODES, SHOW_EVERY, MAX_FRAMES, TRAINED_LEVEL, LOW_RANDOM_THRESHOLD, HIGH_RANDOM_THRESHOLD

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Car Racer AI by AW')

# q learning stuff
#training_mode = False # the flag that determines which function is going to be called (main or train_q_table)

def main():
    clock = pygame.time.Clock()
    run = True
    q_tables = {1: None, 2: None, 3: None}
    start_q_table_level_1 = 'q_table-level-1.pickle'
    start_q_table_level_2 = 'q_table-level-2.pickle'
    start_q_table_level_3 = 'q_table-level-3.pickle'

    # load the q tables from files
    with open(start_q_table_level_1, 'rb') as f:
        q_tables[1] = pickle.load(f)

    with open(start_q_table_level_2, 'rb') as f:
        q_tables[2] = pickle.load(f)

    with open(start_q_table_level_3, 'rb') as f:
        q_tables[3] = pickle.load(f)

    game = Game(WIN)
    pygame.init()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)

            if event.type == pygame.KEYDOWN:
                if not game.gameover:
                    if event.key == pygame.K_LEFT:
                        game.car.turn_left()
                    elif event.key == pygame.K_RIGHT:
                        game.car.turn_right()

        if not game.gameover:
            game.AI_car.action(np.argmax(q_tables[game.level][(game.frames, game.AI_car.dir)])) # q learning stuff - take an action (move_left, move_right or do nothing) based on a q_table for specific game level
            game.update()

        game.render()
        
    pygame.quit()

# q learning stuff
def train_q_table(fps, trained_level, episodes, show_every):
    clock = pygame.time.Clock()
    game = Game(WIN)
    game.train_mode = True
    pygame.init()

    start_q_table = None
    #start_q_table = 'q_table-episodes-10000-level-3-states-16.pickle' # name of a pickle file from which loaded is q table (if None there will be created q table with random values)
    epsilon = EPS_START # randomness threshold (decides if the q learning algorithm takes either the value from q table or random value from specific range)
        # 0.0 (always from q table), 1.0 (always random values)
        # it should be equal 0.0 if start_q_table is different than None

    if start_q_table is None:
        q_table = np.random.uniform(low=LOW_RANDOM_THRESHOLD, high=HIGH_RANDOM_THRESHOLD, size=([MAX_FRAMES, game.AI_car.STATES, CHOICES])) # dims of tensor: all state (observation) dims X action dim (the most internal)
    else:
        # load the q table from a file
        with open(start_q_table, 'rb') as f:
            q_table = pickle.load(f)

    for episode in range(1, episodes + 1):
        # restore the environment
        game.level = trained_level # it has to be before create_cars method
        game.create_cars()
        game.frames = 0
        game.gameover = False # it is not necessary to train but it looks neat when show is True

        if episode % show_every == 0:
            show = True
        else:
            show = False

        print(f'episode: {episode}, epsilon: {epsilon}, show: {show}')

        done = False # changes to True if agent either reaches the goal (collide with finish flag) or hit the track border in the episode
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    print(pos)

            obs = (game.frames, game.AI_car.dir) # current state of the agent

            if np.random.random() > epsilon:
                action = np.argmax(q_table[obs]) # takes the action based on the max reward from q table
            else:
                action = np.random.randint(0, CHOICES) # otherwise takes the random action

            # update the environment
            game.AI_car.action(action)
            game.update()
            
            # calculate the new q value and update the q table with it
            new_obs = (game.frames, game.AI_car.dir) # future state of the agent (after update the env)
            max_future_q = np.max(q_table[new_obs])
            current_q = q_table[obs + (action,)]

            if game.reward == FINISH_FLAG_REWARD:
                 new_q = FINISH_FLAG_REWARD
            elif game.reward == -BORDER_HIT_PENALTY:
                 new_q = -BORDER_HIT_PENALTY
            else:
                new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (game.reward + DISCOUNT * max_future_q)

            q_table[obs + (action,)] = new_q # update q table with the new q value for specific state and action

            # render environment if there is allowed
            if show:
                clock.tick(fps)
                game.render()

            if game.reward == FINISH_FLAG_REWARD or game.reward == -BORDER_HIT_PENALTY:
                done = True
                print(f'Frames: {game.frames}, reward: {game.reward}')

        epsilon *= EPS_DECAY

    # saves the q_table for appropriate game level to the pickle file
    with open(f'q_table-level-{trained_level}.pickle', 'wb') as f:
        pickle.dump(q_table, f)
        print(f'Q table saved as \'q_table-level-{trained_level}\'.pickle')

    pygame.quit()

def main_menu():
    clock = pygame.time.Clock()
    run = True
    pygame.init()
    train_mode_screen = False
    fps = [30, 60, 120, 0]
    fps_num = 0
    trained_level = [1, 2, 3]
    trained_level_num = 0
    episodes = [i for i in range(100, 3100, 100)]
    episodes_num = 0
    show_every = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    show_every_num = 0

    while run:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return (True, ) + (False, ) * 5

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                x, y = pos

                if not train_mode_screen:
                    # play mode button
                    if 220 < x < 580 and 240 < y < 295:
                        run = False

                    # train mode button
                    elif 200 < x < 600 and 504 < y < 560:
                        train_mode_screen = True

                else:
                    # fps left arrow
                    if 239 < x < 266 and 147 < y < 170 and fps_num > 0:
                        fps_num -= 1

                    # trained level left arrow
                    elif 239 < x < 266 and 305 < y < 334 and trained_level_num > 0:
                        trained_level_num -= 1

                    # episodes left arrow
                    elif 239 < x < 266 and 466 < y < 495 and episodes_num > 0:
                        episodes_num -= 1

                    # show every left arrow
                    elif 239 < x < 266 and 626 < y < 655 and show_every_num > 0:
                        show_every_num -= 1

                    # fps right arrow
                    elif 534 < x < 556 and 147 < y < 170 and fps_num < len(fps) - 1:
                        fps_num += 1

                    # trained level right arrow
                    elif 534 < x < 556 and 307 < y < 332 and trained_level_num < len(trained_level) - 1:
                        trained_level_num += 1

                    # episodes right arrow
                    elif 534 < x < 556 and 466 < y < 492 and episodes_num < len(episodes) - 1:
                        episodes_num += 1

                    # show every right arrow
                    elif 534 < x < 556 and 626 < y < 652 and show_every_num < len(show_every) - 1:
                        show_every_num += 1

                    # run training button
                    elif 247 < x < 552 and 700 < y < 739:
                        return False, True, fps[fps_num], trained_level[trained_level_num], \
                            episodes[episodes_num], show_every[show_every_num]

        WIN.fill(ORANGE)
        if not train_mode_screen:
            font = pygame.font.SysFont('comicsans', 90)

            # play mode button
            button = font.render('PLAY MODE', 1, WHITE, BLACK)
            WIN.blit(button, (int(WIDTH/2 - button.get_width()/2),\
                int(HEIGHT/3 - button.get_height()/2)))

            # train mode button
            button = font.render('TRAIN MODE', 1, WHITE, BLACK)
            WIN.blit(button, (int(WIDTH/2 - button.get_width()/2),\
                int(2*HEIGHT/3 - button.get_height()/2)))

        else:
            font = pygame.font.SysFont('comicsans', 40)

            # fps
            text = font.render('FPS:', 1, GREEN)
            WIN.blit(text, (int(WIDTH/2 - text.get_width()/2),\
                int(HEIGHT/10 - text.get_height()/2)))

            field = font.render(f'{fps[fps_num]}', 1, WHITE)
            WIN.blit(field, (int(WIDTH/2 - field.get_width()/2),\
                int(2*HEIGHT/10 - field.get_height()/2)))

            if fps_num > 0:
                pygame.draw.polygon(WIN, BLACK,\
                     [(int(WIDTH/3), int(2*HEIGHT/10 - field.get_height()/2)), \
                    (int(WIDTH/3), int(2*HEIGHT/10 + field.get_height()/2)), \
                    (int(WIDTH/3 - field.get_height()), int(2*HEIGHT/10))])

            if fps_num < len(fps) - 1:
                pygame.draw.polygon(WIN, BLACK, \
                    [(int(2*WIDTH/3), int(2*HEIGHT/10 - field.get_height()/2)), \
                    (int(2*WIDTH/3), int(2*HEIGHT/10 + field.get_height()/2)), \
                    (int(2*WIDTH/3 + field.get_height()), int(2*HEIGHT/10))])

            # trained level
            text = font.render('TRAINED_LEVEL:', 1, GREEN)
            WIN.blit(text, (int(WIDTH/2 - text.get_width()/2),\
                int(3*HEIGHT/10 - text.get_height()/2)))

            field = font.render(f'{trained_level[trained_level_num]}', 1, WHITE)
            WIN.blit(field, (int(WIDTH/2 - field.get_width()/2),\
                int(4*HEIGHT/10 - field.get_height()/2)))

            if trained_level_num > 0:
                pygame.draw.polygon(WIN, BLACK,\
                     [(int(WIDTH/3), int(4*HEIGHT/10 - field.get_height()/2)), \
                    (int(WIDTH/3), int(4*HEIGHT/10 + field.get_height()/2)), \
                    (int(WIDTH/3 - field.get_height()), int(4*HEIGHT/10))])

            if trained_level_num < len(trained_level) - 1:
                pygame.draw.polygon(WIN, BLACK,\
                     [(int(2*WIDTH/3), int(4*HEIGHT/10 - field.get_height()/2)), \
                    (int(2*WIDTH/3), int(4*HEIGHT/10 + field.get_height()/2)), \
                    (int(2*WIDTH/3 + field.get_height()), int(4*HEIGHT/10))])

            # episodes
            text = font.render('EPISODES:', 1, GREEN)
            WIN.blit(text, (int(WIDTH/2 - text.get_width()/2),\
                int(5*HEIGHT/10 - text.get_height()/2)))

            field = font.render(f'{episodes[episodes_num]}', 1, WHITE)
            WIN.blit(field, (int(WIDTH/2 - field.get_width()/2),\
                int(6*HEIGHT/10 - field.get_height()/2)))

            if episodes_num > 0:
                pygame.draw.polygon(WIN, BLACK, \
                    [(int(WIDTH/3), int(6*HEIGHT/10 - field.get_height()/2)), \
                    (int(WIDTH/3), int(6*HEIGHT/10 + field.get_height()/2)), \
                    (int(WIDTH/3 - field.get_height()), int(6*HEIGHT/10))])

            if episodes_num < len(episodes) - 1:
                pygame.draw.polygon(WIN, BLACK, \
                    [(int(2*WIDTH/3), int(6*HEIGHT/10 - field.get_height()/2)), \
                    (int(2*WIDTH/3), int(6*HEIGHT/10 + field.get_height()/2)), \
                    (int(2*WIDTH/3 + field.get_height()), int(6*HEIGHT/10))])

            # show every
            text = font.render('SHOW_EVERY:', 1, GREEN)
            WIN.blit(text, (int(WIDTH/2 - text.get_width()/2),\
                int(7*HEIGHT/10 - text.get_height()/2)))

            field = font.render(f'{show_every[show_every_num]}', 1, WHITE)
            WIN.blit(field, (int(WIDTH/2 - field.get_width()/2),\
                int(8*HEIGHT/10 - field.get_height()/2)))

            if show_every_num > 0:
                pygame.draw.polygon(WIN, BLACK,\
                     [(int(WIDTH/3), int(8*HEIGHT/10 - field.get_height()/2)), \
                    (int(WIDTH/3), int(8*HEIGHT/10 + field.get_height()/2)), \
                    (int(WIDTH/3 - field.get_height()), int(8*HEIGHT/10))])

            if show_every_num < len(show_every) - 1:
                pygame.draw.polygon(WIN, BLACK, \
                    [(int(2*WIDTH/3), int(8*HEIGHT/10 - field.get_height()/2)), \
                    (int(2*WIDTH/3), int(8*HEIGHT/10 + field.get_height()/2)), \
                    (int(2*WIDTH/3 + field.get_height()), int(8*HEIGHT/10))])

            # run button
            font = pygame.font.SysFont('comicsans', 60)
            button = font.render('RUN TRAINING', 1, WHITE, BLACK)
            WIN.blit(button, (int(WIDTH/2 - button.get_width()/2),\
                int(9*HEIGHT/10 - button.get_height()/2)))

        pygame.display.update()   
    
    return (False, ) * 6

quit, training_mode, fps, trained_level, episodes, show_every = main_menu()

if not quit:
    if training_mode:
        train_q_table(fps, trained_level, episodes, show_every)
    else:
        main()
