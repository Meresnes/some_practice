import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    # Создагние экрана и название окна
    pygame.init()
    game_settings = Settings()
    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen, game_settings)

    # Создание группы для хранения пуль и пришельцев
    bullets = Group()
    aliens = Group()

    # Создание флота пиршельцев.
    gf.create_fleet(game_settings, screen, aliens)
    # game loop
    while True:
        # обрабатывает нажатия клавишь и мыши
        gf.check_events(game_settings, screen, ship, bullets)
        ship.update()

        gf.update_bullets(bullets)
        # Обновляет изображение на экране и отображает новый экран
        gf.update_screen(game_settings, screen, ship, aliens,
                         bullets)


run_game()
# Рефакторинг create_feet() страница 263