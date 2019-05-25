import pygame as pg
import pytmx

from settings import TILE_SIZE
from sprite.wall import Wall
from sprite.zombie import Zombie


class TiledMap:
    def __init__(self, file_name):
        self.tiled_map = pytmx.load_pygame(file_name, pixelalpha=True)
        self.width = self.tiled_map.width * TILE_SIZE
        self.height = self.tiled_map.height * TILE_SIZE
        self.scale = TILE_SIZE / self.tiled_map.tilewidth

    def make_map(self):
        temp_surface = pg.Surface((self.width, self.height))
        self._render(temp_surface)
        return temp_surface

    def _render(self, surface):
        tile_by_gid = self.tiled_map.get_tile_image_by_gid
        for layer in self.tiled_map.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid in layer:
                    tile = tile_by_gid(gid)
                    if tile:
                        surface.blit(pg.transform.scale(tile, (TILE_SIZE, TILE_SIZE)), (x * TILE_SIZE, y * TILE_SIZE))


class Map:
    def __init__(self, file_name):
        self.data = []
        with open(file_name, 'rt') as f:
            for line in f:
                self.data.append(line)

        self.tile_with = max(len(_line) for _line in self.data)
        self.tile_height = len(self.data)

        self.width = self.tile_with * TILE_SIZE
        self.height = self.tile_height * TILE_SIZE

    def load(self, game):
        for line, tiles in enumerate(self.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(game, col, line)
                if tile == 'Z':
                    Zombie(game, col * TILE_SIZE, line * TILE_SIZE)
