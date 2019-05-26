from pygame.sprite import Group

from game.sprite.obstacle import Obstacle
from game.sprite.player import Player
from game.sprite.zombie import Zombie
from game.tilemap import TiledMap


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
        self.walls = Group()

        self.map = TiledMap('assets/maps/tomb_of_raspitun/level_1.tmx')
        self.map_image = self.map.make_map()
        self.map_rect = self.map_image.get_rect()

        self.has_menu = False

        for tile_object in self.map.tiled_map.objects:
            if tile_object.name == 'wall':
                self._create_obstacle(tile_object, self.walls)
            elif tile_object.name == 'zombie':
                self._create_zombie(tile_object)
            elif tile_object.name == 'player':
                self._create_player(tile_object)

    def update(self):
        pass

    def events(self, events):
        pass

    def _create_player(self, tile_object):
        self.player = Player(self.game, tile_object.x * self.map.scale, tile_object.y * self.map.scale)

    def _create_zombie(self, tile_object):
        Zombie(self.game, (self.game.all_sprites, self.zombies), tile_object.x * self.map.scale,
               tile_object.y * self.map.scale)

    def _create_obstacle(self, tile_object, group):
        return Obstacle(self.game,
                        group,
                        tile_object.x * self.map.scale,
                        tile_object.y * self.map.scale,
                        tile_object.width * self.map.scale,
                        tile_object.height * self.map.scale)
