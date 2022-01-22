import pygame
import math


class Bullet(pygame.sprite.Sprite):
    image = pygame.image.load('images/bullet.png')

    def __init__(self, rabbit, screen, settings):
        """create new bullet object at rabbit location"""
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.angle = rabbit.angle
        self.image = pygame.transform.rotate(self.image,
                                             360 - self.angle * 57.29)
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.left, self.rect.top = rabbit.rect.centerx, rabbit.rect.centery
        self.speed_factor = settings.bullet_speed_factor

    def update(self):
        """make bullet move to up"""
        velx = math.cos(self.angle) * self.speed_factor
        vely = math.sin(self.angle) * self.speed_factor
        self.rect.left += velx
        self.rect.top += vely

    def draw_bullet(self):
        """draw bullet on the screen"""
        self.screen.blit(self.image, self.rect)

