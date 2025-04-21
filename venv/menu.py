import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from save_file import load_high_score
from backgrounds import Background

# Esta función muestra el menú principal del juego
# Permite al jugador ver su puntaje más alto y elegir entre iniciar el juego o salir
def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    high_score = load_high_score()
    background = Background("backgrounds/background_menu.jpg")

    # Renderiza el menú principal
    # Carga la imagen de fondo y la escala para que se ajuste a la pantalla
    while True:
        screen.blit(background.surface, (0, 0))
        title_text = font.render("ASTEROIDS", True, (255, 255, 255))
        high_score_text = small_font.render(f"High Score: {high_score}", True, (255, 255, 255))
        start_text = small_font.render("Press ENTER to Start", True, (255, 255, 255))
        quit_text = small_font.render("Press ESC to Quit", True, (255, 255, 255))

        # Coloca el texto en la pantalla en posiciones centradas
        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 3))
        screen.blit(high_score_text, (SCREEN_WIDTH // 2 - high_score_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))

        pygame.display.flip()

        # Maneja los eventos de teclado
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        clock.tick(60)