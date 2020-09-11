import pygame
import sys

def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1000,500))
    pygame.display.set_caption("Alien Invasion")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((43, 255, 250))
        pygame.display.flip()
run_game()