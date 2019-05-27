from game.game import *


def new_game():
    global game
    game = Game()
    game.show_start_screen()
    game.show_go_screen()


new_game()
while True:
    game.run()

    if game.game_over:
        game.show_game_over_screen()
        new_game()
