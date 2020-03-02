class GameStats():
    """Track the statistics for alien Invasion"""

    def __init__(self,ai_settings):
        """Initialize statistics."""
        self.ai_setiings = ai_settings
        self.reset_stats()

        #High score should never be reset
        self.high_score = 0


        #start alien invasion in inactive state
        self.game_active = False

    def reset_stats(self):
        """Initialize statistics that can change during the game"""
        self.ships_left = self.ai_setiings.ship_limit
        self.score = 0
