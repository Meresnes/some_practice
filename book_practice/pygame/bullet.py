import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Класс для управления пулями, выпущенными кораблём."""

    def __init__(self, game_settings, screen, ship):
        """Создаёт пули в текущей позиции корабля."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Создание пули в позиции (0, 0) и назначение правильной позиции.
        self.rect = pygame.Rect(0, 0, game_settings.bullet_width,
                                game_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Позиция пули хранится в вещественном формате
        self.y = float(self.rect.y)

        self.color = game_settings.bullet_color
        self.speed_factor = game_settings.bullet_speed_factor
    def update(self):
        """Перемещает пулю вверх по экрану"""
        # Обновление пули в вещ. формате
        self.y -= self.speed_factor
        # Обновление позиции прямоугольника
        self.rect.y = self.y
    def draw_bullet(self):
        """Отрисовка пули"""
        pygame.draw.rect(self.screen, self.color, self.rect)
