import pygame

class Rocket():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('rocket.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()
        #Появление корабля
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        #Флаги для движения
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= 1
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.centery -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)