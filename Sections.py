import sys
from Background import *
width, height = 1080, 720


def terminate():
    pygame.quit()
    sys.exit()


class Screens:
    def run_screen():
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    terminate()
                elif event.type == pygame.KEYDOWN:
                    return  # starting game
                pygame.display.flip()
                clock.tick(FPS)

    def teach_screen():
        intro_text = ["Manuals", '1.Shoot - Left Mouse button.', '2.Skip picture - any key.',]
        fon = pygame.transform.scale(load_image('teach_screen.jpg'), (width, height))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 50)
        text_coord = 90
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('red'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 80
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        Screens.run_screen()

    def final_screen():
        intro_text = ["YOU WON!!!"]
        fon = pygame.transform.scale(load_image('startscreen.png'), (width, height))
        screen.blit(fon, (0, 0))
        Sounds.Music('data1/Sounds/victorymusic.ogg')
        font = pygame.font.Font(None, 100)
        text_coord = 600
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('red'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 300
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        Screens.run_screen()

    def ens_screen():
        intro_text = ["YOU LOST", 'Unfortunately, your flot is devostated, Akbar is dead.',
                      "Now you are going to defend your last base - Tatuin."]
        fon = pygame.transform.scale(load_image('losemenu.jpg'), (width, height))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 50)
        text_coord = 300
        Sounds.Music('data1/Sounds/maintheme.ogg')
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('red'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 0
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        Screens.run_screen()

    def start_screen():
        intro_text = ["STAR WARS: THE ALTERNATIVE STORY", 'Press any key to start']
        Sounds.Music('data1/Sounds/Imperialmarch.ogg')
        fon = pygame.transform.scale(load_image('victorymenu.jpg'), (width, height))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 50)
        text_coord = 400
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('red'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 180
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        Screens.run_screen()

    def complev():
        intro_text = ["You completed level", 'Press any key']
        Sounds.Music('data1/Sounds/Imperialmarch.ogg')
        fon = pygame.transform.scale(load_image('starwr3.jpg'), (width, height))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 50)
        text_coord = 600
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('red'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 350
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        Screens.run_screen()

    def explain():
        intro_text = ["Explanation of plot", 'Your flot tries to get through Imperial defense line to death star.',
                      'Now you are going to have your first battle in space near Jaku.',
                      'Then you have to destroy military factories on Salat.',
                      'And, finally, you will fight on Death Star.']
        fon = pygame.transform.scale(load_image('teach_screen.jpg'), (width, height))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 50)
        text_coord = 200
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('red'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 0
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        Screens.run_screen()

    def total_shit():
        intro_text = ['Game over, Luke is dead']
        fon = pygame.transform.scale(load_image('losemenu.jpg'), (width, height))
        screen.blit(fon, (0, 0))
        font = pygame.font.Font(None, 50)
        text_coord = 600
        Sounds.Music('data1/Sounds/maintheme.ogg')
        for line in intro_text:
            string_rendered = font.render(line, 1, pygame.Color('red'))
            intro_rect = string_rendered.get_rect()
            text_coord += 10
            intro_rect.top = text_coord
            intro_rect.x = 250
            text_coord += intro_rect.height
            screen.blit(string_rendered, intro_rect)
        Screens.run_screen()





