import pygame

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # Inicializa el objeto CircleShape
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        # Defines el contenedor de sprites para el objeto
        # Llama al constructor de la clase padre (pygame.sprite.Sprite)

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius
        # Inicializa la posición, velocidad y radio del objeto

    def draw(self, screen):
        pass
        # Método para dibujar el objeto en la pantalla

    def update(self, dt):
        pass
        # Método para actualizar el objeto en cada frame

    def is_colliding(self, other):
        distance = self.position.distance_to(other.position)
        return distance <= (self.radius + other.radius)
        # Método para verificar si el objeto colisiona con otro objeto
        # Calcula la distancia entre los dos objetos y verifica si es menor o igual a la suma de sus radios
        # Devuelve True si colisionan, False si no