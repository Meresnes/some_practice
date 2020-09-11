import sys
import pygame

def game_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
            if event.key == pygame.K_UP:
                ship.moving_up = True
            if event.key == pygame.K_DOWN:
                ship.moving_down = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
            if event.key == pygame.K_UP:
                ship.moving_up = False
            if event.key == pygame.K_DOWN:
                ship.moving_down = False

def update_screen(screen, ship):
    """Обновляет изображение на экране и отображает новый экран"""
    #При каждом проходе цикла обновляет экран
    screen.fill((255, 255, 250))
    ship.blitme()
    #отображение последнего прорисованного экрана
    pygame.display.flip()

