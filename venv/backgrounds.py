import pygame
from constants import *

class Background:
    def __init__(self, image_path):
        self.surface = pygame.image.load(image_path).convert()
        self.surface = pygame.transform.scale(self.surface, (SCREEN_WIDTH, SCREEN_HEIGHT))
        # Carga la imagen de fondo y la escala a las dimensiones de la pantalla

    def draw(self, screen):
        screen.blit(self.surface, (0, 0))
        # Dibuja la imagen de fondo en la pantalla en la posición (0, 0)