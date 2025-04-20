import pygame
from circleshape import CircleShape
from constants import *


class Player(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.position = pygame.Vector2(x, y)
        self.radius = radius
        self.rotation = 0
        self.shoot_cooldown_timer = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,255,255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(dt)
        # Se verifica si la tecla de disparo está presionada

        if self.shoot_cooldown_timer > 0:
            self.shoot_cooldown_timer -= dt
            # Se reduce el temporizador de recarga de disparo

    def move(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position += forward * PLAYER_SPEED * dt
        if keys[pygame.K_s]:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            self.position -= forward * PLAYER_SPEED * dt
        
    def shoot(self):
        if self.shoot_cooldown_timer > 0:
            return
        # Se verifica si el temporizador de recarga de disparo es mayor que 0
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * SHOT_SPEED
        self.shoot_cooldown_timer = PLAYER_BULLET_COOLDOWN
        # Se crea una instancia de la clase Shot con la posición y velocidad dadas
        # Se asigna una velocidad al disparo en la dirección en la que está mirando el jugador

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 0, 0), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        # Se actualiza la posición del disparo según su velocidad y el tiempo transcurrido)
        # Se dibuja el disparo en la pantalla