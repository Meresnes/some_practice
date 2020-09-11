import sys
import pygame

def game_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.K_DOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
        elif event.type == pygame.K_UP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False