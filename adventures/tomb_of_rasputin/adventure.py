from pygame.sprite import Group, spritecollide

from adventures.tomb_of_rasputin.level import Level1
from game.sprite.obstacle import Obstacle
from game.sprite.player import Player
from game.sprite.zombie import Zombie


def info(game):
    return {'name': 'Tomb of Rasputin', 'adventure': TombOfRasputinFactory(game)}


class TombOfRasputinFactory:
    def __init__(self, game):
        self.game = game

    def execute(self):
        self.game.update_adventure(TombOfRasputin(self.game))


class TombOfRasputin:
    def __init__(self, game, level=Level1):
        self.game = game
        self.zombies = Group()
        self.bullets = Group()
        self.walls = Group()

        self.has_menu = False
        self.updated = False
        self.finish = False

        self.player = None

        # before all assert, create a level
        self._next_level(level(self))

    def update(self):
        self._actual.info()
        self.game_over()

        self.updated = True

    def events(self, events):
        if self._actual.finish():
            if not self._actual.is_end():
                self.game.show_ended_screen()
                self._next_level(self._actual.next_level())
                self.game.show_go_screen()
            else:
                self.finish = True

    def game_over(self):
        if spritecollide(self.player, self.zombies, False) and self.updated:
            self.game.game_over = True

    def create_player(self, tile_object):
        self.player = Player(self.game, tile_object.x * self.map.scale, tile_object.y * self.map.scale)

    def create_zombie(self, tile_object):
        Zombie(self.game, (self.game.all_sprites, self.zombies), tile_object.x * self.map.scale,
               tile_object.y * self.map.scale)

    def create_obstacle(self, tile_object):
        return Obstacle(self.game,
                        self.walls,
                        tile_object.x * self.map.scale,
                        tile_object.y * self.map.scale,
                        tile_object.width * self.map.scale,
                        tile_object.height * self.map.scale)

    def _next_level(self, level):
        self._actual = level

        self.map = self._actual.map
        self.map_image = self._actual.map.make_map()
        self.map_rect = self.map_image.get_rect()

        if self.player:
            self.player.kill()

        self._actual.load_objects()

        self.updated = False
