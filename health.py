import pygame


class HealthBar:
    def __init__(self, screen):
        self.image = pygame.image.load('images/healthbar.png')
        self.fill_image = pygame.image.load('images/health.png')
        self.screen = screen

    def draw_health(self, stat):
        """draw health on the screen"""
        self.screen.blit(self.image, (5, 5))
        for i in range(stat.health_point):
            self.screen.blit(self.fill_image, (i+8, 8))
