import sys
import pygame

def cheсk_events(ship):
    """Обрабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #Когда нажата клавиша двигать корабль
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                #Переместить корабль вправо
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                #Переместить корабль влево
                ship.moving_left = True
        #Когда клавиша отпущена , прекратить движение корабля
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            if event.key == pygame.K_LEFT:
                ship.moving_left = False


def update_screen(game_settings, screen, ship):
    """Обновляет изображение на экране и отображает новый экран"""
    #При каждом проходе цикла обновляет экран
    screen.fill(game_settings.bg_color)
    ship.blitme()
    #отображение последнего прорисованного экрана
    pygame.display.flip()