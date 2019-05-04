from game.game import *

g = Game()
g.show_start_screen()
while True:
    g.run()
    g.show_go_screen()
