import pygame
from cc.constants import WIDTH, HEIGHT, FPS

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Car Racer v1.0 by AW')

def main():
    clock = pygame.time.Clock()
    run = True
    #game = Game(WIN)
    
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)

    pygame.quit()

main()
