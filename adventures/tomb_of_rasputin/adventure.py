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
        self.game.update_level(TombOfRasputin(self.game))


class TombOfRasputin:
    def __init__(self, game):
        self.game = game
        self.zombies = Group()
        self.bullets = Group()
        self.walls = Group()

        self._actual = Level1(self)

        self.map = self._actual.map
        self.map_image = self._actual.map.make_map()
        self.map_rect = self.map_image.get_rect()

        self.has_menu = False
        self.updated = False

        self.player = None

        # before all assert, create a game objects
        self._actual.load_objects()

    def update(self):
        self._actual.info()
        self.game_over()

        if self._actual.next_level():
            print('next level')

        self.updated = True

    def events(self, events):
        pass

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
