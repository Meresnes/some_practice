import pygame
from pygame.sprite import Sprite


class bullet(Sprite):
    """Класс для управления пулями, выпущенными кораблём."""

    def __init__(self, game_settings, screen, ship):
        """Создаёт пули в текущей позиции корабля."""
        super(bullet, self).__init__()
        self.screen = screen

        # Создание пули в позиции (0, 0) и назначение правильной позиции.
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width,
                                game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        # Остановился здесь 249 страница