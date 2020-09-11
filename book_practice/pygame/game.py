import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    #Создагние экрана и название окна
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width,game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(screen, game_settings)

    while True:
        #обрабатывает нажатия клавишь и мыши
        gf.cheсk_events(ship)
        ship.update()
        #Обновляет изображение на экране и отображает новый экран
        gf.update_screen(game_settings, screen, ship)


run_game()