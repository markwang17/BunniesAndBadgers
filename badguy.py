import pygame
import random


class Badguy(pygame.sprite.Sprite):
    image = pygame.image.load('images/badguy.png')

    def __init__(self, screen, settings):
        pygame.sprite.Sprite.__init__(self)
        self.damage = pygame.mixer.Sound("audio/explode.wav")
        self.hit = pygame.mixer.Sound("audio/enemy.wav")
        self.damage.set_volume(0.05)
        self.hit.set_volume(0.05)
        self.rect = self.image.get_rect()
        self.screen = screen
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left = settings.screen_width
        self.rect.top = random.randint(50, settings.screen_height - 50)
        self.speed = settings.badguy_speed_factor

    def update(self):
        self.rect.left -= self.speed

    def draw_badguy(self):
        """draw badguy on the screen"""
        self.screen.blit(self.image, self.rect)
