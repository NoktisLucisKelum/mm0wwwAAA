import pygame
width, height = 1080, 720


class Level:
    def __init__(self, image_file):
        self.image = pygame.transform.scale(pygame.image.load(image_file), (width, height))
