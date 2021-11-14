import pygame
from cc.constants import WIDTH, HEIGHT, FPS
from cc.game import Game

# q learning stuff
import numpy as np
import pickle
from cc.constants import CHOICES, FINISH_FLAG_REWARD, BORDER_HIT_PENALTY, EPS_START, EPS_DECAY, LEARNING_RATE, DISCOUNT, EPISODES, SHOW_EVERY, MAX_FRAMES, TRAINED_LEVEL, LOW_RANDOM_THRESHOLD, HIGH_RANDOM_THRESHOLD

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Car Racer AI by AW')

# q learning stuff
training_mode = False # the flag that determines which function is going to be called (main or train_q_table)

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

    print(q_tables)

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
def train_q_table():
    clock = pygame.time.Clock()
    game = Game(WIN)
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

    for episode in range(1, EPISODES + 1):
        # restore the environment
        game.level = TRAINED_LEVEL # it has to be before create_cars method
        game.create_cars()
        game.frames = 0
        game.gameover = False # it is not necessary to train but it looks neat when show is True

        if episode % SHOW_EVERY == 0:
            show = True
        else:
            show = False

        print(f'episode: {episode}, epsilon: {epsilon}, show: {show}')

        done = False # changes to True if agent either reaches the goal (collide with finish flag) or hit the track border in the episode
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

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
                clock.tick(FPS)
                game.render()

            if game.reward == FINISH_FLAG_REWARD or game.reward == -BORDER_HIT_PENALTY:
                done = True
                print(f'Frames: {game.frames}, reward: {game.reward}')

        epsilon *= EPS_DECAY

    # saves the q_table for appropriate game level to the pickle file
    with open(f'q_table-level-{TRAINED_LEVEL}.pickle', 'wb') as f:
        pickle.dump(q_table, f)

    pygame.quit()

if training_mode:
    train_q_table()
else:
    main()
