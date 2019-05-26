from pygame.sprite import Group

from game.tilemap import TiledMap
from sprite.player import Player
from sprite.obstacle import Obstacle
from sprite.zombie import Zombie


class Home:
    def __init__(self, game):
        self.walls = Group()
        self.zombies = Group()

        self.map = TiledMap('maps/tiled1.tmx')
        self.map_image = self.map.make_map()
        self.map_rect = self.map_image.get_rect()

        for tile_object in self.map.tiled_map.objects:
            if tile_object.name == 'player':
                self.player = Player(game, tile_object.x * self.map.scale, tile_object.y * self.map.scale)
            if tile_object.name == 'wall':
                Obstacle(game,
                         self.walls,
                         tile_object.x * self.map.scale,
                         tile_object.y * self.map.scale,
                         tile_object.width * self.map.scale,
                         tile_object.height * self.map.scale)
            if tile_object.name == 'zombie':
                Zombie(game, (game.all_sprites, self.zombies), tile_object.x * self.map.scale,
                       tile_object.y * self.map.scale)
