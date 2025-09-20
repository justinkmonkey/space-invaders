import pygame
import sys
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_hight))
    pygame.display.set_caption("Alien Invasion")
  
    ship = Ship(screen)
    # Start the main loop for the game.
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)
run_game()