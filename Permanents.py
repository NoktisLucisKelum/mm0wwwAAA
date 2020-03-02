from Animation import *
import Variables


class Sounds:
    def Sound(x):
        b = pygame.mixer.Sound(x)
        b.play()

    def Music(x):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(x)
        pygame.mixer.music.play(-1)


def healthpo(screen):
    font = pygame.font.Font(None, 30)
    text = font.render("Здоровье: " + str(Variables.hp), 1, (100, 255, 100))
    text_x = width - text.get_width() + 50
    text_y = text.get_height()
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (0, 255, 0), (text_x, 2 * text_y + 20,
                                           text_w, text_h + 20), 1)
    pygame.draw.rect(screen, (0, 255, 0), (text_x, 2 * text_y + 25,
                                           abs((text_w * Variables.hp) // 20), text_h))

V = 500
FPS = 120
WIDTH, HEIGHT = 1080, 720

size = WIDTH, HEIGHT

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

# Player sprites
FirstPlayNoFire = pygame.transform.scale(sprite_sheet('hand.png', 159, 130, (1, 1))[0], (400, 400))
FirstPlayFire = pygame.transform.scale(sprite_sheet('hand.png', 159, 130, (1, 1), (166, 0))[0], (400, 400))
DrawMouseImage = load_image("aim234.png", -1)




# Enemies sprites
width = 150
height = width * 2
RedStormTrooperNoFire = pygame.transform.scale(load_image("redStormTrooper1.png", -1), (width, height))
RedStormTrooperFire = pygame.transform.scale(load_image('redStormTrooper2.png', -1), (width, height))
ResD = pygame.transform.scale(load_image('boom.png', -1), (width, height))
Tf = pygame.transform.scale(load_image("fighter1.png", -1), (width, 170))
Tf1 = pygame.transform.scale(load_image('fighter2.png', -1), (width, 170))
pygame.mixer.init()
fire_sound = pygame.mixer.Sound('data1/shotgun4.wav')

