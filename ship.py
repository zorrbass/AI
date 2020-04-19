import pygame


class Ship:
    """class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and its starting position"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # load the ship image and get its screen rect.
        # more ships at https://www.ex-astris-scientia.org/scans.htm
        self.image = pygame.image.load("images/ship3.bmp")
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen:
        self.rect.midbottom = self.screen_rect.midbottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position based on the movement flag."""
        if self.moving_right:
            self.rect.x += 1
        elif self.moving_left:
            self.rect.x -= 1


    def blitme(self):
        """Draw the ship at its curren position."""
        self.screen.blit(self.image, self.rect)

