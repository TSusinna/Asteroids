import pygame

class CircleShape(pygame.sprite.Sprite):
    # Clase para representar un objeto circular en el juego
    # Hereda de pygame.sprite.Sprite para poder usar el sistema de sprites de Pygame
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        # Inicializa la posición, velocidad y radio del objeto
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        pass

    def update(self, dt):
        pass

    # Verifica si el objeto colisiona con otro objeto circular
    # Calcula la distancia entre los dos objetos y compara con la suma de sus radios
    # Si la distancia es menor o igual a la suma de los radios, hay colisión
    def is_colliding(self, other):
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius)