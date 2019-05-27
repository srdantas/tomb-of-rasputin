from game.game import *

game = Game()
game.show_start_screen()
while True:
    game.run()

    if game.game_over:
        game.game_over_screen()
        game = Game()
