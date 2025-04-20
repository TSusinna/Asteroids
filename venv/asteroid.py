from circleshape import CircleShape
from constants import *
import pygame
import random
# Importa la libreria pygame y lo necesario para este archivo

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        # Llama al constructor de la clase padre (CircleShape) y le pasa los argumentos x, y y radius

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
        # Dibuja un círculo en la pantalla con el color blanco, la posición y el radio del asteroide
        # El último argumento es el grosor del borde del círculo
        # Si es 0, el círculo se rellena completamente

    def update(self, dt):
        self.position += self.velocity * dt
        # Actualiza la posición del asteroide multiplicando su velocidad por el tiempo delta (dt)
        # Esto hace que el asteroide se mueva a lo largo de su trayectoria

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # Si el radio del asteroide es menor o igual al radio mínimo, no se divide
        # Si no, se divide en dos asteroides más pequeños

        random_angle = random.uniform(20, 50)
        # Genera un ángulo aleatorio entre 20 y 50 grados

        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
        # Rota la velocidad del asteroide en el ángulo aleatorio y en su negativo
        # Esto crea dos nuevas velocidades para los nuevos asteroides

        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2
        # Crea dos nuevos asteroides con la posición y el radio del asteroide original
        # Asigna las nuevas velocidades a los nuevos asteroides