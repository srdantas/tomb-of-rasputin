import pygame as pg
import pytmx

from settings import TILE_SIZE


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
