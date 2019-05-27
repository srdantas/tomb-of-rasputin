from pygame.sprite import Group, spritecollide

from game.label import Label
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
        self.bullets = Group()
        self.walls = Group()

        self.map = TiledMap('assets/maps/tomb_of_raspitun/level_1.tmx')
        self.map_image = self.map.make_map()
        self.map_rect = self.map_image.get_rect()

        self.has_menu = False
        self.updated = False

        for tile_object in self.map.tiled_map.objects:
            if tile_object.name == 'wall':
                self._create_obstacle(tile_object, self.walls)
            elif tile_object.name == 'zombie':
                self._create_zombie(tile_object)
            elif tile_object.name == 'player':
                self._create_player(tile_object)

    def update(self):
        self._info()
        self.game_over()

        self.updated = True

    def events(self, events):
        pass

    def game_over(self):
        if spritecollide(self.player, self.zombies, False) and self.updated:
            self.game.game_over = True

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

    def _info(self):
        self.game.infos.append(Label('Level 1', "assets/fonts/blocks.ttf", 10, 10, font_size=42))
        self.game.infos.append(
            Label(f'Zombies: {len(self.zombies)}', "assets/fonts/pixel_square.ttf", 10, 80, font_size=24))
