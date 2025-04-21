import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, HIGH_SCORE
from menu import main_menu
from save_file import load_high_score, save_high_score
from backgrounds import Background

def defeat_screen(score):

    high_score = load_high_score()
    if score > high_score:
        high_score = score
        save_high_score(high_score)
        # Guarda el nuevo puntaje más alto en el archivo


    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()
    # Inicia pygame y crea una ventana con el tamaño definido en SCREEN_WIDTH y SCREEN_HEIGHT
    # Crea fuentes para el texto del menú y un reloj para controlar la velocidad de fotogramas

    while True:
        background = Background("backgrounds/background_menu.jpg")
        screen.blit(background.surface, (0, 0))
        # Carga una imagen de fondo y la dibuja en la pantalla

       
        game_over_text = font.render("GAME OVER", True, (255, 0, 0))
        score_text = small_font.render(f"Your Score: {score}", True, (255, 255, 255))
        restart_text = small_font.render("Press ENTER to Restart", True, (255, 255, 255))
        quit_text = small_font.render("Press ESC to Quit", True, (255, 255, 255))
        # Renderiza el texto del menú principal, incluyendo el título, el puntaje más alto y las instrucciones para iniciar o salir del juego

        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 3))
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))
        # Dibuja el texto en la pantalla en posiciones centradas


        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main_menu()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()
        # Maneja los eventos de teclado y clics del mouse

        clock.tick(60)