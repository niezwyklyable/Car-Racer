import pygame
from cc.constants import WIDTH, HEIGHT, FPS
from cc.game import Game

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Car Racer by AW')

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

main()
