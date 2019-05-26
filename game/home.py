from pygame.sprite import Group

from game.label import Label
from game.sprite.obstacle import Obstacle
from game.sprite.player import Player
from game.tilemap import TiledMap
from settings import BLACK


class Home:
    def __init__(self, game):
        self.walls = Group()
        self.zombies = Group()

        self.map = TiledMap('assets/maps/home.tmx')
        self.map_image = self.map.make_map()
        self.map_rect = self.map_image.get_rect()

        for tile_object in self.map.tiled_map.objects:
            if tile_object.name == 'wall':
                self._create_obstacle(game, tile_object)
            elif tile_object.name == 'exit':
                self._create_exit(game, tile_object)
            elif tile_object.name == 'adventurer':
                self._create_adventurer(game, tile_object)
            elif tile_object.name == 'ranking':
                self._create_ranker(game, tile_object)
            elif tile_object.name == 'player':
                self._create_player(game, tile_object)

    def _create_player(self, game, tile_object):
        self.player = Player(game, tile_object.x * self.map.scale, tile_object.y * self.map.scale)

    def _create_adventurer(self, game, tile_object):
        game.labels.append(
            Label('Adventurer', 'assets/fonts/blocks.ttf', (tile_object.x - tile_object.width) * self.map.scale,
                  (tile_object.y + tile_object.height) * self.map.scale, font_size=16, color=BLACK))
        self._create_obstacle(game, tile_object)

    def _create_ranker(self, game, tile_object):
        game.labels.append(
            Label('Ranking', 'assets/fonts/blocks.ttf', (tile_object.x - tile_object.width) * self.map.scale,
                  tile_object.y * self.map.scale, font_size=16, color=BLACK))
        self._create_obstacle(game, tile_object)

    def _create_exit(self, game, tile_object):
        game.labels.append(
            Label('Exit', 'assets/fonts/future_narrow.ttf', (tile_object.x + (tile_object.width / 2)) * self.map.scale,
                  tile_object.y * self.map.scale, font_size=16, color=BLACK))
        self._create_obstacle(game, tile_object)

    def _create_obstacle(self, game, tile_object):
        Obstacle(game,
                 self.walls,
                 tile_object.x * self.map.scale,
                 tile_object.y * self.map.scale,
                 tile_object.width * self.map.scale,
                 tile_object.height * self.map.scale)
