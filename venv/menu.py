import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from save_file import load_high_score, save_high_score

def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    # Inicia pygame y crea una ventana con el tamaño definido en SCREEN_WIDTH y SCREEN_HEIGHT
    # Crea fuentes para el texto del menú y un reloj para controlar la velocidad de fotogramas

    high_score = load_high_score()
    # Carga el puntaje más alto desde el archivo de guardado

    while True:
        screen.fill((0, 0, 0))

        title_text = font.render("ASTEROIDS", True, (255, 255, 255))
        dev_name_text = small_font.render("By: Tomás Susinna", True, (255, 255, 255))
        high_score_text = small_font.render(f"High Score: {high_score}", True, (255, 255, 255))
        start_text = small_font.render("Press ENTER to Start", True, (255, 255, 255))
        quit_text = small_font.render("Press ESC to Quit", True, (255, 255, 255))
        # Renderiza el texto del menú principal, incluyendo el título, el puntaje más alto y las instrucciones para iniciar o salir del juego

        screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, SCREEN_HEIGHT // 3))
        screen.blit(high_score_text, (SCREEN_WIDTH // 2 - high_score_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(dev_name_text, (SCREEN_WIDTH // 2 - dev_name_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))
        # Dibuja el texto en la pantalla en posiciones centradas

        pygame.display.flip()

        # Handle events
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
        # Maneja los eventos de teclado y clics del mouse

        clock.tick(60)