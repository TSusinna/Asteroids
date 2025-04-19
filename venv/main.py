import pygame
from constants import *
from player import Player
# Se importa la librería de pygame y el contenido de constants.py para utilizarse en este archivo

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Se inicia pygame y se define el tamaño de la pantalla utilizando las constantes definidas en constants.py

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    # Se inicia pygame y se define el tamaño de la pantalla utilizando las constantes definidas en constants.py

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    # Se crea una instancia de la clase Player, que representa al jugador, en el centro de la pantalla

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        screen.fill((0, 0, 0))
        player.draw(screen)
        pygame.display.flip()

        dt = clock.tick(60) / 1000
        # Se inicia un reloj para controlar la tasa de refresco de la pantalla a 60 FPS
# Se inicia un bucle infinito que escucha eventos de pygame y cierra la ventana si se recibe un evento de cierre
# Se llena la pantalla de color negro todo el tiempo




if __name__ == "__main__":
    main()
# Si el script se ejecuta directamente, se llama a la función main()