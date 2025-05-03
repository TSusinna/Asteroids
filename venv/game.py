# Importa las clases necesarias para el juego
import pygame
from constants import *
from player import Player, Shot
from asteroid import Asteroid
from asteroidfield import AsteroidField
from backgrounds import Background
from defeat_screen import defeat_screen
from sound import play_gameplay_music, stop_music

class Game:
    # Inicializa pygame y crea una ventana con el tamaño definido en SCREEN_WIDTH y SCREEN_HEIGHT
    # Crea un reloj para controlar la velocidad de fotogramas
    # Define el puntaje inicial y el estado de ejecución del juego
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.score = 0
        self.running = True
        play_gameplay_music()

        # Carga una imagen de fondo y la escala a las dimensiones de la pantalla
        self.background = Background("textures/background_game.jpg")
        self.background.darken()

        # Crea grupos de sprites para objetos actualizables y dibujables
        self.updatable = pygame.sprite.Group()
        self.drawable = pygame.sprite.Group()
        self.shots = pygame.sprite.Group()
        self.asteroids = pygame.sprite.Group()

        # Asigna las clases a los grupos correspondientes
        Player.containers = (self.updatable, self.drawable)
        Shot.containers = (self.shots, self.updatable, self.drawable)
        Asteroid.containers = (self.updatable, self.drawable, self.asteroids)
        AsteroidField.containers = self.updatable

        # Crea una instancia de la clase Player en el centro de la pantalla
        # y una instancia de la clase AsteroidField para generar asteroides
        self.player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
        self.asteroid_field = AsteroidField()

        # Se inicializa el tiempo delta (dt) a 0
        self.dt = 0
        # Se carga una fuente para mostrar el puntaje en la pantalla
        self.font = pygame.font.Font(None, 36)

    # Se define un método para manejar los eventos del juego
    # Se verifica si se cierra la ventana del juego
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

    # Se define un método para actualizar los objetos del juego
    # Se actualizan los objetos en el grupo de sprites actualizables
    def update(self, dt):
        self.updatable.update(dt)

    # Se define un método para dibujar los objetos en la pantalla
    # Se dibuja el fondo y una superposición oscura sobre la pantalla
    # Se dibuja el puntaje en la esquina superior izquierda de la pantalla
    def draw(self):
        self.screen.blit(self.background.surface, (0, 0))
        dark_overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        dark_overlay.set_alpha(100)
        dark_overlay.fill((0, 0, 0))
        self.screen.blit(dark_overlay, (0, 0))
        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))

        # Se dibujan los objetos en el grupo de sprites dibujables
        for obj in self.drawable:
            obj.draw(self.screen)

        pygame.display.flip() # Actualiza la pantalla para mostrar los cambios

    # Se define un método para verificar las colisiones entre el jugador y los asteroides
    def check_collisions(self):
        for asteroid in self.asteroids:
            if self.player.is_colliding(asteroid):
                defeat_screen(self.score)
                self.running = False
                return

            for shot in self.shots:
                if asteroid.is_colliding(shot):
                    asteroid.split()
                    shot.kill()
                    self.score += 1

    # Se define un método para ejecutar el juego
    # Se ejecuta un bucle principal que controla la lógica del juego
    # Se limita la velocidad de fotogramas a 60 FPS y se calcula el tiempo delta (dt)
    # Se manejan los eventos, se actualizan los objetos, se verifican las colisiones y se dibujan los objetos en la pantalla
    # Se repite hasta que se cierra la ventana del juego
    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000
            self.handle_events()
            self.update(dt)
            self.check_collisions()
            self.draw()
        stop_music()