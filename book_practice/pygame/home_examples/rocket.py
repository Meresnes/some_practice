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
        self.move_right = False
        self.move_left = False

    def rocket_move(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 1


    def blitme(self):
        self.screen.blit(self.image, self.rect)