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
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        # Respond to keypresses and mouse movements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False



    def _update_screen(self):
        """Update images on the screen, and flip to the new screen"""
        # Sets the background color to bg_color
        self.screen.fill(self.settings.bg_color)
        # After the background draw the ship so it is visible on top
        self.ship.blitme()

        # Make the most recently drawn screen visible
        pygame.display.flip()


if __name__ == "__main__":
    '''Make a game instance and run the game'''
    ai = AlienInvasion()
    ai.run_game()
