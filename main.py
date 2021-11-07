import pygame
from cc.maths import WIDTH, HEIGHT
from cc.game import Game

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Car Racer by AW')
FPS = 30

def main():
    clock = pygame.time.Clock()
    run = True
    game = Game(WIN)
    
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)

        game.update()
        game.render()
        
    pygame.quit()

main()
