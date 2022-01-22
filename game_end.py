import pygame


class GameEnding:
    def __init__(self, screen):
        self.screen = screen
        self.gameover = pygame.image.load('images/gameover.png')
        self.gamewin = pygame.image.load('images/youwin.png')
        self.which_end = None

    def draw_over(self):
        self.screen.blit(self.gameover, (0, 0))

    def draw_win(self):
        self.screen.blit(self.gamewin, (0, 0))
