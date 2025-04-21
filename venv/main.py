from menu import main_menu
from game import Game

# Este es el punto de entrada principal del juego
# Aquí se inicializa el juego y se muestra el menú principal
if __name__ == "__main__":
    while True:
        main_menu()
        game = Game()
        game.run()