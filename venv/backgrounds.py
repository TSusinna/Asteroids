# Importar las bibliotecas necesarias
import pygame
from constants import *

# Definir la clase Background
# Esta clase se encarga de cargar y dibujar la imagen de fondo del juego
class Background:
    def __init__(self, image_path):
        self.surface = pygame.image.load(image_path).convert()
        self.surface = pygame.transform.scale(self.surface, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw(self, screen):
        screen.blit(self.surface, (0, 0))

    # Oscurece  el fondo
    def darken(self):
        dark_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        dark_overlay.set_alpha(200)
        dark_overlay.fill((0, 0, 0))
        return dark_overlay