import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, HIGH_SCORE
from menu import main_menu
from save_file import load_high_score, save_high_score

def defeat_screen(score):

    high_score = load_high_score()
    if score > high_score:
        high_score = score
        save_high_score(high_score)
    """
    Displays the defeat screen with the player's score and allows them to return to the main menu or quit.
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    clock = pygame.time.Clock()

    while True:
        screen.fill((0, 0, 0))  # Black background

        # Render defeat screen text
        game_over_text = font.render("TE MORISTE PELOTUDO JAJAJAJAJAJAJAJAA", True, (255, 0, 0))
        score_text = small_font.render(f"Your Score: {score}", True, (255, 255, 255))
        restart_text = small_font.render("Press ENTER to Restart", True, (255, 255, 255))
        quit_text = small_font.render("Press ESC to Quit", True, (255, 255, 255))
        # Blit text to the screen
        screen.blit(game_over_text, (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 3))
        screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))
        screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(quit_text, (SCREEN_WIDTH // 2 - quit_text.get_width() // 2, SCREEN_HEIGHT // 2 + 100))


        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:  # Restart the game
                    main_menu()
                if event.key == pygame.K_ESCAPE:  # Quit the game
                    pygame.quit()
                    exit()

        clock.tick(60)