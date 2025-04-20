import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
# Se importa la librería de pygame y el contenido de necesario para usarse en este archivo

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    # Se inicia pygame y se define el tamaño de la pantalla utilizando las constantes definidas en constants.py

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    # Se crean grupos de sprites para objetos actualizables y dibujables
    # Se asigna la clase Player a los grupos de sprites para que se puedan actualizar y dibujar

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    # Se crea un grupo de asteroides y se asigna la clase Asteroid a los grupos de sprites para que se puedan actualizar y dibujar
    # Se asigna la clase AsteroidField al grupo de sprites actualizables
    # Se crea una instancia de la clase AsteroidField

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    # Se crea una instancia de la clase Player en el centro de la pantalla

    dt = 0
    # Se inicializa el tiempo delta (dt) a 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Se verifica si se ha cerrado la ventana y se sale del programa

        updatable.update(dt)
        # Se actualizan los objetos en el grupo updatable

        screen.fill((0, 0, 0)) #También puede usarse "black"
        for object in drawable:
            object.draw(screen)
        pygame.display.flip()
        # Se dibujan los objetos en el grupo drawable en la pantalla
        # Se actualiza la pantalla

        dt = clock.tick(60) / 1000
        # Se limita la velocidad de fotogramas a 60 FPS y se calcula el tiempo delta

if __name__ == "__main__":
    main()
    # Si el script se ejecuta directamente, se llama a la función main()