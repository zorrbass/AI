class Settings:
    """A class to store all settings for Alien Invasion"""
    def __init__(self):
        """Initialize the games settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (100, 120, 150)

        # Ship settings
        self.ship_speed = 1.4
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = (55, 255, 0)
        self.bullets_allowed = 3

        # Alien settings
        self.alien_speed = 0.2
        self.fleet_drop_speed = 50
        # fleet direction 1 means right, -1 means left
        self.fleet_direction = 1
