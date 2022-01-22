import pygame
import math


class Rabbit:
    def __init__(self, screen):
        self.shoot = pygame.mixer.Sound("audio/shoot.wav")
        self.image = pygame.image.load('images/dude.png')
        self.shoot.set_volume(0.05)
        self.rotateimg = self.image
        self.rect = self.image.get_rect()
        self.roteterect = self.rect
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.angle = 0

    def update(self):
        """change location due to moving marks"""
        if self.moving_right:
            self.rect.centerx += 2
        if self.moving_left:
            self.rect.centerx -= 2
        if self.moving_up:
            self.rect.centery -= 2
        if self.moving_down:
            self.rect.centery += 2

    def update_toward(self):
        position = pygame.mouse.get_pos()
        self.angle = math.atan2(position[1] - self.rect.centery + 32,
                                position[0] - self.rect.centerx + 26)
        self.rotateimg = pygame.transform.rotate(self.image, 360-self.angle*57.29)
        self.roteterect = (self.rect.centerx - self.rotateimg.get_rect().width/2,
                           self.rect.centery - self.rotateimg.get_rect().height/2)

    def blitme(self):
        """display rabbit at the location"""
        self.screen.blit(self.rotateimg, self.roteterect)
