
import pygame as pg
from random import randint
from math import atan2, pi, sin, cos, radians


pg.init()

boost_force = 12
patron_force = 50
screen_width = 800
screen_height = 800
indent = 150

mouse_pos = (-1, -1)
speed_x = 0
speed_y = 0
running_game = False
first_game = True
ammo = 3
score = 0
button_pressed = False
paused = False


screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Bruner')
clock = pg.time.Clock()
font_1 = pg.font.Font('OpenSans-Bold.ttf', 98)
font_2 = pg.font.Font('OpenSans-Bold.ttf', 60)
font_3 = pg.font.Font('OpenSans-Bold.ttf', 560)

penguin_surf = pg.image.load('penguin.png').convert_alpha()
welcome_surf = font_1.render('WELCOME', True, 'gray')
click_surf = font_2.render('Click to start', True, 'gray')
lose_surf = font_1.render(f'Your score: {score}', True, 'gray')
ammo_count_surf = font_3.render(f'{ammo}', True, '#f3f3f3')
score_surf = font_2.render(f'Score: {score}', True, '#d6d6d6')
ammo_surf = pg.image.load('ammo.png').convert_alpha()
apple_surf = pg.image.load('64x_apple1.png').convert_alpha()
gun_serf = pg.image.load('128x_gun.png').convert_alpha()
paused_serf = font_1.render('PAUSED', True, '#D5637E')
patron_serf = pg.image.load('128x_patron.png').convert_alpha()
rotated_patron_serf = patron_serf
pause_pause_sef = font_2.render('Press any key to pause', True, '#d6d6d6')


def pifagor(a, b):
    return int((a**2+b**2)**0.5)


def update():
    global ammo_count_rect, ammo_count_surf, score_rect, score_surf, lose_rect
    ammo_count_surf = font_3.render(f'{ammo}', True, '#f3f3f3')
    score_surf = font_2.render(f'Score: {score}', True, '#d6d6d6')
    ammo_count_rect = ammo_count_surf.get_rect(center=(screen_width // 2, 375))
    score_rect = score_surf.get_rect(midbottom=(screen_width // 2, 750))
    lose_rect = lose_surf.get_rect(midbottom=(screen_width // 2, screen_height // 2 - 20))


def get_ammo():
    global ammo_rect_1, ammo_rect_2
    ammo_rect_1 = ammo_surf.get_rect(midbottom=(randint(indent, screen_width - indent), randint(indent, screen_height - indent)))
    while len(penguin_rect.collidelistall([ammo_rect_1])) != 0:
        ammo_rect_1 = ammo_surf.get_rect(midbottom=(randint(indent, screen_width - indent), randint(indent, screen_height - indent)))
    ammo_rect_2 = ammo_surf.get_rect(midbottom=(randint(indent, screen_width - indent), randint(indent, screen_height - indent)))
    while len(penguin_rect.collidelistall([ammo_rect_1, ammo_rect_2])) != 0 or ammo_rect_1.colliderect(ammo_rect_2):
        ammo_rect_2 = ammo_surf.get_rect(midbottom=(randint(indent, screen_width - indent), randint(indent, screen_height - indent)))


def get_apple():
    global apple_rect
    apple_rect = ammo_surf.get_rect(midbottom=(randint(64, screen_width - 64), randint(100, screen_height - 100)))
    while len(penguin_rect.collidelistall([ammo_rect_1, ammo_rect_2])) != 0:
        apple_rect = ammo_surf.get_rect(midbottom=(randint(64, screen_width - 64), randint(100, screen_height - 100)))


def start():
    global penguin_rect, welcome_rect, click_rect, lose_rect, ammo_count_rect, score_rect, ammo_rect_1, ammo_rect_2,\
        ammo_rect, patron_rect, ammo, score, speed_x, speed_y, patron_speed_x, patron_speed_y, pause_rect
    screen.fill('white')
    penguin_rect = penguin_surf.get_rect(midbottom=(screen_width//2, screen_height//2))
    welcome_rect = welcome_surf.get_rect(midbottom=(screen_width//2, screen_height//2))
    click_rect = click_surf.get_rect(midbottom=(screen_width//2, screen_height//2+60))
    lose_rect = lose_surf.get_rect(midbottom=(screen_width//2, screen_height//2-20))
    ammo_count_rect = ammo_count_surf.get_rect(center=(screen_width//2, 450))
    score_rect = score_surf.get_rect(midbottom=(screen_width//2, 750))
    patron_rect = patron_serf.get_rect(center=(-100, -100))
    pause_rect = pause_pause_sef.get_rect(center=(screen_width//2, 60))

    ammo = 3
    score = 0
    speed_x = 0
    speed_y = 0
    penguin_rect.x = 350
    penguin_rect.y = 200
    patron_speed_x = 0
    patron_speed_y = 0


start()


while True:

    for event in pg.event.get():

        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.MOUSEBUTTONDOWN and running_game:
            button_pressed = True
        if event.type == (pg.MOUSEBUTTONDOWN or event.type == pg.KEYDOWN) and not running_game:
            running_game = True
            alr_started = True
            first_game = False
            start()
        if event.type == pg.MOUSEMOTION:
            mouse_pos = event.pos
            mouse_x = mouse_pos[0]
            mouse_y = mouse_pos[1]
        if event.type == pg.KEYDOWN and running_game:
            paused = True if paused is False else False

    if running_game and not paused:  # in game

        screen.fill('white')

        if alr_started:
            get_ammo()
            get_apple()
            alr_started = False

        update()

        screen.blit(pause_pause_sef, pause_rect)
        screen.blit(ammo_count_surf, ammo_count_rect)
        screen.blit(score_surf, score_rect)

        hypotenuse = pifagor(abs(mouse_x - penguin_rect.x), abs(mouse_y - penguin_rect.y))
        sin_for_x = abs(mouse_x - penguin_rect.x) / hypotenuse
        cos_for_y = abs(mouse_y - penguin_rect.y) / hypotenuse

        screen.blit(ammo_surf, ammo_rect_1)
        screen.blit(ammo_surf, ammo_rect_2)
        screen.blit(apple_surf, apple_rect)

        angle = 360 - atan2(mouse_y - penguin_rect.y, mouse_x - penguin_rect.x) * 180 / pi  # calculating angle

        rotated_gun = pg.transform.rotate(gun_serf, angle)  # making rotating gun
        rotated_gun_rect = rotated_gun.get_rect(center=penguin_rect.center)

        if button_pressed and ammo > 0:  # controlling penguin
            update()
            speed_x *= 0.5
            speed_y = 0

            speed_x += cos(radians(angle)) * boost_force
            speed_y += sin(radians(angle)) * boost_force
            ammo -= 1

            patron_rect = patron_serf.get_rect(center=penguin_rect.center)
            patron_speed_x = + cos(radians(angle)) * patron_force
            patron_speed_y = - sin(radians(angle)) * patron_force

            patron_rect.x += patron_speed_x
            patron_rect.y += patron_speed_y

            rotated_patron_serf = pg.transform.rotate(patron_serf, angle)

        patron_rect.x += patron_speed_x
        patron_rect.y += patron_speed_y
        screen.blit(rotated_patron_serf, patron_rect)

        if len(penguin_rect.collidelistall([ammo_rect_1, ammo_rect_2])) != 0:  # collides with ammo
            ammo += 1
            get_ammo()

        if penguin_rect.colliderect(apple_rect):  # collides with apple
            score += 1
            lose_surf = font_1.render(f'Your score: {score}', True, 'gray')
            get_apple()

        screen.blit(rotated_gun, rotated_gun_rect)
        screen.blit(penguin_surf, penguin_rect)

        speed_y += 0.25  # gravity
        penguin_rect.y += speed_y
        penguin_rect.x -= speed_x
        if penguin_rect.centerx >= screen_width - 64:
            penguin_rect.centerx = screen_width - 65
            speed_x *= -1
        if penguin_rect.centerx <= 64:
            penguin_rect.centerx = 65
            speed_x *= -1
        if penguin_rect.y > screen_height + 50:
            running_game = False

    elif not paused:  # in menu / after lose
        screen.fill('white')
        if first_game:  # first try
            screen.blit(welcome_surf, welcome_rect)
            screen.blit(click_surf, click_rect)
        else:  # after lose
            update()
            screen.blit(lose_surf, lose_rect)
            screen.blit(click_surf, click_rect)

    elif paused and running_game:
        paused_rect = paused_serf.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(paused_serf, paused_rect)

    button_pressed = False
    pg.display.update()
    clock.tick(60)
