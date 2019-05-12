from game.sprites import Wall
from settings import *


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
