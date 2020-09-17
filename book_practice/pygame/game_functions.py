import sys
import pygame
from bullet import Bullet


def check_keydown_event(event, game_settings, screen, ship, bullets):
    """Реагирует на нажатие клавиш"""
    if event.key == pygame.K_RIGHT:
        # Переместить корабль вправо
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        # Переместить корабль влево
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # Создание новой пули и включение её в группу bullets.
        fire_bullet(game_settings, screen, ship, bullets)


def check_keyup_event(event, ship):
    """Реагирует на отпускание клавиш"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(game_settings, screen, ship, bullets):
    """Обрабатывает нажатия клавиш и события мыши"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        # Когда нажата клавиша двигать корабль
        elif event.type == pygame.KEYDOWN:
            check_keydown_event(event, game_settings, screen, ship, bullets)
        # Когда клавиша отпущена , прекратить движение корабля
        elif event.type == pygame.KEYUP:
            check_keyup_event(event, ship)


def fire_bullet(game_settings, screen, ship, bullets):
    """Выпускает пулю, если максимум ещё не достигнут"""
    if len(bullets) < game_settings.bullet_allowed:
        new_bullet = Bullet(game_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(bullets):
    """Обновляет позиции пуль и удаляет те, которые вышли за экран"""
    bullets.update()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)


def update_screen(game_settings, screen, ship, bullets):
    """Обновляет изображение на экране и отображает новый экран"""
    # При каждом проходе цикла обновляет экран
    screen.fill(game_settings.bg_color)
    # Пули выводяться позадиизображения корабля и пришельцев
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # отображение последнего прорисованного экрана
    pygame.display.flip()
