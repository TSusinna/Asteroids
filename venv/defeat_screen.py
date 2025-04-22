import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from menu import main_menu
from save_file import load_high_score, save_high_score
from backgrounds import Background

def defeat_screen(score):
    # Esta función se encarga de mostrar la pantalla de derrota
    # Busca el puntaje más alto guardado y lo compara con el puntaje actual
    # Si el puntaje actual es mayor, lo guarda como el nuevo puntaje más alto
    high_score = load_high_score()
    if score > high_score:
        high_score = score
        save_high_score(high_score)

    # Inicializa Pygame y crea una ventana para mostrar la pantalla de derrota
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    # Carga la imagen de fondo y la escala para que se ajuste a la pantalla
    # Crea un objeto Background para manejar la imagen de fondo
    while True:
        background = Background("textures/background_menu.jpg")
        screen.blit(background.surface, (0, 0))

        # Escribe el texto de "GAME OVER" y el puntaje en la pantalla
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        score_text = small_font.render(f"Your Score: {score}", True, (255, 255, 255))
        restart_text = small_font.render("Press ENTER to go to the Main Menu", True, (255, 255, 255))
        quit_text = small_font.render("Press ESC to Quit", True, (255, 255, 255))

        # Coloca el texto en la pantalla en posiciones centradas
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 3))
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))

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

        # Define la velocidad de fotogramas
        clock.tick(60)