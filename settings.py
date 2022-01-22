class Settings:
    """
    The game settings of Bunnies and Badgers. Most of attributes are static.
    badguy_generate_speed is dynamic.
    """
    def __init__(self):
        self.screen_width = 640
        self.screen_height = 480
        self.bg_color = (230, 230, 230)
        self.bullet_speed_factor = 10
        self.badguy_speed_factor = 3
        # 0 to 20, take 100-x to generate
        self.badguy_generate_speed = 0
