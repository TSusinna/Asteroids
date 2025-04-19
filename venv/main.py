import pygame
from constants import *
# Se importa la librería de pygame y el contenido de constants.py para utilizarse en este archivo

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# Se inicia pygame y se define el tamaño de la pantalla utilizando las constantes definidas en constants.py

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
if __name__ == "__main__":
    main()
# Se define la función main() que imprime un mensaje de inicio y las dimensiones de la pantalla.
# Si el script se ejecuta directamente, se llama a la función main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
    screen.fill((0, 0, 0))
    pygame.display.flip()
# Se inicia un bucle infinito que escucha eventos de pygame y cierra la ventana si se recibe un evento de cierre
# Se llena la pantalla de color negro todo el tiempo