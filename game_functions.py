import sys
from time import sleep
import pygame
from bullet import Bullet
from badguy import Badguy


def check_events(rabbit, stat, arrow_group, screen, settings):
    """check keyboard and mouse events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, rabbit)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, rabbit)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # shoot sound
            stat.accuracy[1] += 1
            arrow = Bullet(rabbit, screen, settings)
            rabbit.shoot.play()
            arrow_group.add(arrow)


def check_keydown_events(event, rabbit):
    """check keydown events"""
    if event.key == pygame.K_d:
        rabbit.moving_right = True
    elif event.key == pygame.K_a:
        rabbit.moving_left = True
    elif event.key == pygame.K_w:
        rabbit.moving_up = True
    elif event.key == pygame.K_s:
        rabbit.moving_down = True
    elif event.key == pygame.K_SPACE:
        pass
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, rabbit):
    """check keyup events"""
    if event.key == pygame.K_d:
        rabbit.moving_right = False
    elif event.key == pygame.K_a:
        rabbit.moving_left = False
    elif event.key == pygame.K_w:
        rabbit.moving_up = False
    elif event.key == pygame.K_s:
        rabbit.moving_down = False


def check_generate_badguy(stat, setting, badguy_group, screen):
    if stat.badtimer == 0:
        badguy = Badguy(screen, setting)
        badguy_group.add(badguy)
        stat.badtimer = 100 - (setting.badguy_generate_speed * 2)
        setting.badguy_generate_speed = 20 if setting.badguy_generate_speed >= 20 else setting.badguy_generate_speed + 2
    stat.badtimer -= 1


def check_game_over(stat, game_end):
    if pygame.time.get_ticks() >= 90000:
        stat.game_on = False
        game_end.which_end = True
    if stat.health_point <= 0:
        stat.game_on = False
        game_end.which_end = False


def show_ending(screen, exitcode, stat, game_ending):
    font = pygame.font.Font(None, 24)
    stat.compute_accuracy()
    text = font.render(f"Accuracy: {stat.percentage}%", True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.centery = screen.get_rect().centery + 24
    while True:
        screen.fill(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if exitcode:
            game_ending.draw_win()
        else:
            game_ending.draw_over()
        screen.blit(text, text_rect)
        pygame.display.flip()


def update_grass(bb_settings, screen, grass):
    for x in range(bb_settings.screen_width//grass.image.get_width()+1):
        for y in range(bb_settings.screen_height//grass.image.get_height()+1):
            screen.blit(grass.image, (x*grass.image.get_width(),
                                      y*grass.image.get_height()))


def update_castle(bb_settings, screen, castle):
    for y in range(25, (bb_settings.screen_height - 30),
                   (castle.image.get_height()+5)):
        screen.blit(castle.image, (0, y))


def update_badguys(badguy_group, arrow_group, stat):
    for badguy in badguy_group:
        badguy.update()
        # the number 64 is from the width of the castle
        if badguy.rect.left < 64:
            badguy_group.remove(badguy)
            stat.health_point -= 7
            badguy.damage.play()
        for arrow in arrow_group:
            if pygame.sprite.collide_mask(badguy, arrow):
                arrow_group.remove(arrow)
                badguy_group.remove(badguy)
                stat.accuracy[0] += 1
                badguy.hit.play()
        badguy.draw_badguy()


def update_arrows(arrow_group, settings):
    for arrow in arrow_group:
        arrow.update()
        if arrow.rect.right < 0 or arrow.rect.left > settings.screen_width or arrow.rect.top > settings.screen_height or arrow.rect.bottom < 0:
            arrow_group.remove(arrow)
        arrow.draw_bullet()


def update_screen(bb_settings, screen, rabbit, grass, castle, arrow_group,
                  stat, badguy_group, health_bar, time_bar, game_end):
    """update images on screen and switch to new screen"""
    # fill new screen in loops
    screen.fill(bb_settings.bg_color)
    update_grass(bb_settings, screen, grass)
    update_castle(bb_settings, screen, castle)
    health_bar.draw_health(stat)
    time_bar.update()
    time_bar.drawtext()
    update_arrows(arrow_group, bb_settings)
    update_badguys(badguy_group, arrow_group, stat)
    check_generate_badguy(stat, bb_settings, badguy_group, screen)
    rabbit.update()
    rabbit.update_toward()
    rabbit.blitme()
    check_game_over(stat, game_end)
    # if inactive, display PLAY button
    # if not stats.game_active:
    #     play_button.draw_button()
    # display new screen
    if game_end.which_end is not None:
        show_ending(screen, game_end.which_end, stat, game_end)
    pygame.display.flip()
