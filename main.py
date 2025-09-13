import pygame
import sys
from settings import Settings



def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_hight))
    pygame.display.set_caption("Alien Invasion")
    bg_color = "blue"
   
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(ai_settings.bg_color)
        # Make the most recently drawn screen visible.
        pygame.display.flip()
run_game()