import pygame


class Ship:
    """class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and its starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its screen rect.
        # more ships at https://www.ex-astris-scientia.org/scans.htm
        self.image = pygame.image.load("images/ship3.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen:
        self.rect.midbottom = self.screen_rect.midbottom

        # Store decimal value for the ship's horizontal position (self.rect.x)
        self.x = float(self.rect.x)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position based on the movement flag."""
        # Update the ship's  x value not the rect which follows in the next line
        # setting the max movement to 0 left and screen width minus img size
        if self.moving_right and self.x < self.settings.screen_width-44:
            self.x += self.settings.ship_speed
        if self.moving_left and self.x > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at its curren position."""
        self.screen.blit(self.image, self.rect)

