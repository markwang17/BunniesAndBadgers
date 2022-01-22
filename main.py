import pygame
from settings import Settings
import game_functions as gf
from rabbit import Rabbit
from grass import Grass
from castle import Castle
from gamestat import Stat
from health import HealthBar
from timebar import TimeBar
from game_end import GameEnding


def run_game():
    pygame.init()
    pygame.mixer.init()
    bb_settings = Settings()
    grass = Grass()
    castle = Castle()
    stat = Stat()
    arrow_sprites_group = pygame.sprite.Group()
    badguy_sprites_group = pygame.sprite.Group()
    screen = pygame.display.set_mode((bb_settings.screen_width,
                                      bb_settings.screen_height))
    game_end = GameEnding(screen)
    health_bar = HealthBar(screen)
    time_bar = TimeBar(screen)
    rabbit = Rabbit(screen)
    pygame.display.set_caption("Bunnies and Badgers")

    pygame.mixer.music.load('audio/moonlight.wav')
    pygame.mixer.music.play(-1, 0.0)
    pygame.mixer.music.set_volume(0.25)

    while stat.game_on:
        gf.check_events(rabbit, stat, arrow_sprites_group, screen, bb_settings)
        gf.update_screen(bb_settings, screen, rabbit, grass, castle,
                         arrow_sprites_group, stat, badguy_sprites_group,
                         health_bar, time_bar, game_end)


run_game()
