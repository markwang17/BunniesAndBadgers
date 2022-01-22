import pygame


class TimeBar:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 24)
        self.text = self.font.render(str((pygame.time.get_ticks())//60000)
                                     + ':' +
                                     str((pygame.time.get_ticks())//1000%60)
                                     .zfill(2), True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.topright = [635, 5]

    def update(self):
        self.text = self.font.render(str((90000-pygame.time.get_ticks()) // 60000)
                                     + ':' +
                                     str((90000-pygame.time.get_ticks()) // 1000 % 60)
                                     .zfill(2), True, (0, 0, 0))

    def drawtext(self):
        self.screen.blit(self.text, self.text_rect)
