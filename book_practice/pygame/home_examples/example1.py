import pygame
import sys
from rocket import Rocket
import game_functions as gf
def run_game():
    pygame.init()
    screen = pygame.display.set_mode((1000,500))
    pygame.display.set_caption("Ship Invasion")
    ship = Rocket(screen)

    while True:
        gf.game_events(ship)
        ship.update()

        gf.update_screen(screen,ship)
run_game()