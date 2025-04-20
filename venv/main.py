import pygame
from constants import *
from player import Player, Shot
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
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    # Se crean grupos de sprites para objetos actualizables y dibujables
    # Se asigna la clase Player a los grupos de sprites para que se puedan actualizar y dibujar
    # Se asigna la clase Shot a los grupos de sprites para que se puedan actualizar y dibujar
    # Se asigna la clase Asteroid a los grupos de sprites para que se puedan actualizar y dibujar
    # Se asigna la clase AsteroidField a los grupos de sprites para que se puedan actualizar

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    # Se crea una instancia de la clase Player en el centro de la pantalla

    dt = 0
    asteroid_field = AsteroidField()
    # Se inicializa el tiempo delta (dt) a 0
    # Se crea una instancia de la clase AsteroidField para generar asteroides

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

        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game Over!")
                pygame.quit()
                exit()
        # Se verifica si el jugador ha colisionado con algún asteroids

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.is_colliding(shot):
                    print("Asteroid destroyed!")
                    asteroid.split()
                    shot.kill()
        # Se verifica si un disparo ha colisionado con un asteroide

if __name__ == "__main__":
    main()
    # Si el script se ejecuta directamente, se llama a la función main()