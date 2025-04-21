# Importa la libreria pygame y lo necesario para este archivo
from circleshape import CircleShape
from constants import *
import pygame
import random


class Asteroid(CircleShape):
    # Llama al constructor de la clase padre (CircleShape) y le pasa los argumentos x, y y radius
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    # Dibuja un círculo en la pantalla con el color blanco, la posición y el radio del asteroide
    # El último argumento es el grosor del borde del círculo
    # Si es 0, el círculo se rellena completamente
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    # Actualiza la posición del asteroide multiplicando su velocidad por el tiempo delta (dt)
    # Esto hace que el asteroide se mueva a lo largo de su trayectoria
    def update(self, dt):
        self.position += self.velocity * dt

    # Divide el asteroide en dos nuevos asteroides
    # Primero mata el asteroide original y luego verifica si su radio es menor o igual al radio mínimo
    # Si es así, no hace nada
    # Si no, genera un ángulo aleatorio entre 20 y 50 grados
    # Luego rota la velocidad del asteroide en ese ángulo y en su negativo
    # Esto crea dos nuevas velocidades para los nuevos asteroides
    # Finalmente, crea dos nuevos asteroides con la posición y el radio del asteroide original
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        random_angle = random.uniform(20, 50)
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2