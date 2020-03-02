
class Settings:

    """A class to store all setiings for Alien Invasion."""
    
    def __init__(self):

        """Initialize the game's static settings"""
        #screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #Bullet setting
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        #alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #Fleet directionof 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #How quickly the game speed up
        self.speedup_scale = 1.1
        #How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that chaned throughout the game"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #Fleet_direction of 1 represent right; -1 represent left.
        self.fleet_direction =1

        #scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settingsand alien point values."""
        self.ship_speed_factor *=self.speedup_scale
        self.bullet_speed_factor *=self.speedup_scale
        self.alien_speed_factor *=self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)