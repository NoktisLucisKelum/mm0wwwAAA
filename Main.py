from levels import *


def delete():
    Screens.ens_screen()
    mouse_sprite = pygame.sprite.Group()
    whiteStormTroopers_sprite = pygame.sprite.Group()
    firstPlay_sprite = pygame.sprite.Group()
    player_sprite = pygame.sprite.Group()
    backGround_sprite = pygame.sprite.Group()
    tie_fighter_sprite = pygame.sprite.Group()
    Variables.hp = 20
    cantina_level()

pygame.init()
Screens.start_screen()
Screens.teach_screen()
Screens.explain()
x = mn1()
if x == 1:
    delete()
else:
    Screens.complev()
    y = mn3()
    if y == 1:
        delete()
    else:
        Screens.complev()
        z = mn2()
        if z == 1:
            delete()
