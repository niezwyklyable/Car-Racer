import pygame
from cc.constants import WIDTH, HEIGHT, FPS
from cc.game import Game

# q learning stuff
import numpy as np
import pickle
from cc.constants import CHOICES, FINISH_FLAG_REWARD, BORDER_HIT_PENALTY, EPS_START, EPS_DECAY, LEARNING_RATE, DISCOUNT, EPISODES, SHOW_EVERY

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Car Racer by AW')

# q learning stuff
training_mode = True # the flag that determines which function is going to be called (main or train_q_table)

def main():
    clock = pygame.time.Clock()
    run = True
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
            game.update()

        game.render()
        
    pygame.quit()

# q learning stuff
def train_q_table():
    clock = pygame.time.Clock()
    game = Game(WIN)
    pygame.init()

    start_q_table = None # name of a pickle file from which loaded is q table (if None there will be created q table with random values)
    epsilon = EPS_START # randomness threshold (decides if the q learning algorithm takes either the value from q table or random value from specific range)
        # 0.0 (always from q table), 1.0 (always random values)
        # it should be equal 0.0 if start_q_table is different than None
    trained_level = 0 # level to be trained

    if start_q_table is None:
        q_table = np.random.uniform(low=-5, high=0, size=([WIDTH, HEIGHT, CHOICES])) # dims of tensor: all state (observation) dims X action dim (the most internal)
    else:
        # load the q table from a file
        with open(start_q_table, 'rb') as f:
            q_table = pickle.load(f)

    for episode in range(EPISODES):
        # restore the environment
        game.create_cars()
        game.level = trained_level
        game.frames = 0
        game.gameover = False

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

            obs = (np.int(game.AI_car.x), np.int(game.AI_car.y)) # current state of the agent

            if np.random.random() > epsilon:
                action = np.argmax(q_table[obs]) # takes the action based on the max reward from q table
            else:
                action = np.random.randint(0, CHOICES) # otherwise takes the random action

            # update the environment
            game.AI_car.action(action)
            game.update()
            
            # calculate the new q value and update the q table with it
            new_obs = (np.int(game.AI_car.x), np.int(game.AI_car.y)) # future state of the agent (after update the env)
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

        epsilon *= EPS_DECAY

    # saves the q_table for appropriate game level to the pickle file
    with open(f'q_table-level-{trained_level}.pickle', 'wb') as f:
        pickle.dump(q_table, f)

    pygame.quit()

if training_mode:
    train_q_table()
else:
    main()
