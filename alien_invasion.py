import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        # create an instance of class Settings
        self.settings = Settings()

        # create a screen with parameters from setting
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_hight))

        pygame.display.set_caption("Wolf's Alien Invasion")

        # Create an instance of class Ship
        self.ship = Ship(self)

    def run_game(self):
        """Start the main loop for the game"""
        while True:
            # Watch for keyboard and mouse movements
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop
            # Sets the background color to bg_color
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Make the most recently drawn screen visible
            pygame.display.flip()


if __name__ == "__main__":
    '''Make a game instance and run the game'''
    ai = AlienInvasion()
    ai.run_game()
