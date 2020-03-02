from Player import *
from Enemy import *
from Background import *
from Sections import Screens
n = ['swds1.png', 'swds2.png', 'swds3.png']


def mn3():
    Background(backGround_sprite, 'darlevel.jpg', (1080, 730))
    enemy = 10
    enemy_event = 30
    t = 0
    pygame.time.set_timer(enemy_event, 2500)
    FirstPlay(firstPlay_sprite)
    Enemy(whiteStormTroopers_sprite, 150, 50, 350, 450)
    DrawMouse(mouse_sprite)
    x, y = 500, 320
    running = True
    Sounds.Music('data1/Sounds/maintheme.ogg')
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                fire_sound.set_volume(0.6)
                fire_sound.play()
                firstPlay_sprite.update(pygame.mouse.get_focused(), True)
                whiteStormTroopers_sprite.update(True, event.pos)
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
            if event.type == enemy_event and enemy != 0:
                Enemy(whiteStormTroopers_sprite, 150, 50, 900, 450)
                enemy -= 1
        if Variables.hp <= 0:
            t = 1
            running = False
        elif enemy == 0:
            t = 2
            Variables.hp = 20
            running = False
        backGround_sprite.draw(screen)
        firstPlay_sprite.update(pygame.mouse.get_focused(), False)
        whiteStormTroopers_sprite.update()
        whiteStormTroopers_sprite.draw(screen)
        mouse_sprite.update(x, y, pygame.mouse.get_focused())
        firstPlay_sprite.draw(screen)
        mouse_sprite.draw(screen)
        healthpo(screen)
        clock.tick(FPS)
        pygame.display.update()
    if t == 1:
        return 1


def mn1():
    Background(backGround_sprite, 'space.png', (1080, 720))
    enemy = 10
    t = 0
    enemy_event = 30
    pygame.time.set_timer(enemy_event, 2500)
    TieFight(tie_fighter_sprite, 150, 50, 350, 450)
    DrawMouse(mouse_sprite)
    x, y = 500, 320
    running = True
    Sounds.Music('data1/Sounds/normal soundtrack.ogg')
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                fire_sound.set_volume(0.6)
                fire_sound.play()
                firstPlay_sprite.update(pygame.mouse.get_focused(), True)
                tie_fighter_sprite.update(True, event.pos)
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
            if event.type == enemy_event and enemy != 0:
                TieFight(tie_fighter_sprite, 150, 50, 900, 450)
                enemy -= 1
        if Variables.hp <= 0:
            t = 1
            running = False
        elif enemy == 0:
            t = 2
            Variables.hp = 20
            running = False
        backGround_sprite.draw(screen)
        firstPlay_sprite.update(pygame.mouse.get_focused(), False)
        tie_fighter_sprite.update()
        tie_fighter_sprite.draw(screen)
        mouse_sprite.update(x, y, pygame.mouse.get_focused())
        mouse_sprite.draw(screen)
        healthpo(screen)
        clock.tick(FPS)
        pygame.display.update()
    if t == 1:
        return 1


def mn2():
    s = 0
    t = 0
    Background(backGround_sprite, n[s], (1080, 720))
    enemy = 10
    enemy_event = 30
    pygame.time.set_timer(enemy_event, 2500)
    TieFight(tie_fighter_sprite, 150, 50, 350, 450)
    DrawMouse(mouse_sprite)
    x, y = 500, 320
    running = True
    Sounds.Music('data1/Sounds/normal soundtrack.ogg')
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                fire_sound.set_volume(0.6)
                fire_sound.play()
                tie_fighter_sprite.update(True, event.pos)
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
            if event.type == enemy_event and enemy != 0:
                TieFight(tie_fighter_sprite, 150, 50, 900, 450)
                enemy -= 1
        if Variables.hp <= 0:
            t = 1
            running = False
        elif enemy == 0:
            t = 2
            Variables.hp = 20
            running = False
        s += 1
        s = s % 3
        Background(backGround_sprite, n[s], (1080, 730))
        backGround_sprite.draw(screen)
        tie_fighter_sprite.update()
        tie_fighter_sprite.draw(screen)
        mouse_sprite.update(x, y, pygame.mouse.get_focused())
        mouse_sprite.draw(screen)
        healthpo(screen)
        clock.tick(200)
        pygame.display.update()
    if t == 1:
        return 1
    elif t == 2:
        Screens.final_screen()


def cantina_level():
    Background(backGround_sprite, 'Dune Sea level1.png', (1080, 720))
    enemy = 10
    t = 0
    enemy_event = 30
    pygame.time.set_timer(enemy_event, 2500)
    FirstPlay(firstPlay_sprite)
    Enemy(whiteStormTroopers_sprite, 150, 50, 350, 450)
    DrawMouse(mouse_sprite)
    x, y = 500, 320
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                fire_sound.set_volume(0.6)
                fire_sound.play()
                firstPlay_sprite.update(pygame.mouse.get_focused(), True)
                whiteStormTroopers_sprite.update(True, event.pos)
            if event.type == pygame.MOUSEMOTION:
                x, y = event.pos
            if event.type == enemy_event and enemy != 0:
                Enemy(whiteStormTroopers_sprite, 150, 50, 900, 450)
                enemy -= 1
        if Variables.hp <= 0:
            t = 1
            running = False
        elif enemy == 0:
            t = 2
            Variables.hp = 20
            running = False
        backGround_sprite.draw(screen)
        firstPlay_sprite.update(pygame.mouse.get_focused(), False)
        whiteStormTroopers_sprite.update()
        whiteStormTroopers_sprite.draw(screen)
        mouse_sprite.update(x, y, pygame.mouse.get_focused())
        firstPlay_sprite.draw(screen)
        mouse_sprite.draw(screen)
        healthpo(screen)
        clock.tick(FPS)
        pygame.display.update()
    if t == 1:
        Screens.total_shit()
    elif t == 2:
        Screens.complev()