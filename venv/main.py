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
    # Se crea un objeto de reloj para controlar la velocidad de fotogramas

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    # Se crean grupos de sprites para objetos actualizables y dibujables. Luego se asignan las clases a los grupos correspondientes de cada una


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    # Se crea una instancia de la clase Player en el centro de la pantalla

    dt = 0     # Se inicializa el tiempo delta (dt) a 0
    asteroid_field = AsteroidField()     # Se crea una instancia de la clase AsteroidField para generar asteroides
    font = pygame.font.Font(None, 36)     # Se carga una fuente para mostrar el puntaje en la pantalla
    global SCORE # Se define una variable global SCORE para almacenar el puntaje del jugador

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                SCORE = 0
                pygame.quit()
                exit()
            # Se verifica si se ha cerrado la ventana y se sale del programa

        updatable.update(dt)
        # Se actualizan los objetos en el grupo updatable

        screen.fill((0, 0, 0)) #También puede usarse "black"
        for object in drawable:
            object.draw(screen)
        # Se dibujan los objetos en el grupo drawable en la pantalla

        score_text = font.render(f"Score: {SCORE}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        pygame.display.flip()
        # Se dibuja el texto del puntaje en la pantalla en la posición (10, 10)
        # Se actualiza la pantalla

        dt = clock.tick(60) / 1000
        # Se limita la velocidad de fotogramas a 60 FPS y se calcula el tiempo delta

        for asteroid in asteroids:
            if player.is_colliding(asteroid):
                print("Game Over!")
                SCORE = 0
                pygame.quit()
                exit()
        # Se verifica si el jugador ha colisionado con algún asteroids

        for asteroid in asteroids:
            for shot in shots:
                if asteroid.is_colliding(shot):
                    print("Asteroid destroyed!")
                    asteroid.split()
                    shot.kill()
                    SCORE += 1
        # Se verifica si un disparo ha colisionado con un asteroide
        # Si es así, se destruye el asteroide y el disparo
        # Se divide el asteroide en dos más pequeños
        # Se incrementa el puntaje



if __name__ == "__main__":
    main()
    # Si el script se ejecuta directamente, se llama a la función main()