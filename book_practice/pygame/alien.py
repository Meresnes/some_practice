import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс, представляющий одного пршельца"""

    def __init__(self, game_settings, screen):
        """Инициализирует пришельца и задаёт ему начальную позицию"""
        super(Alien, self).__init__()
        self.screen = screen
        self.game_settings = game_settings

        # Загрузка изображение пришельца
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в верхнем вернем углу экрана.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной позиции пришельца
        self.x = float(self.rect.x)


    def blime(self):
        """Выводит пришельца в текущей позиции"""
        self.screen.blit(self.image, self.rect)