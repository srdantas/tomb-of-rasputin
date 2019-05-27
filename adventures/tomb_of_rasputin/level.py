from game.label import Label
from game.tilemap import TiledMap


class Level1:
    def __init__(self, adventure):
        self.adventure = adventure
        self.map = TiledMap('assets/maps/tomb_of_rasputin/level_1.tmx')

    def load_objects(self):
        for tile_object in self.map.tiled_map.objects:
            if tile_object.name == 'wall':
                self.adventure.create_obstacle(tile_object)
            elif tile_object.name == 'zombie':
                self.adventure.create_zombie(tile_object)
            elif tile_object.name == 'player':
                self.adventure.create_player(tile_object)

    def info(self):
        self.adventure.game.infos.append(Label('Level 1', "assets/fonts/blocks.ttf", 10, 10, font_size=42))
        self.adventure.game.infos.append(
            Label(f'Zombies: {len(self.adventure.zombies)}', "assets/fonts/pixel_square.ttf", 10, 80, font_size=24))

    def finish(self):
        return len(self.adventure.zombies) == 0

    def next_level(self):
        return Level2(self.adventure)

    @staticmethod
    def is_end():
        return False


class Level2:
    def __init__(self, adventure):
        self.adventure = adventure
        self.map = TiledMap('assets/maps/tomb_of_rasputin/level_2.tmx')

    def load_objects(self):
        for tile_object in self.map.tiled_map.objects:
            if tile_object.name == 'wall':
                self.adventure.create_obstacle(tile_object)
            elif tile_object.name == 'zombie':
                self.adventure.create_zombie(tile_object)
            elif tile_object.name == 'player':
                self.adventure.create_player(tile_object)

    def info(self):
        self.adventure.game.infos.append(Label('Level 2', "assets/fonts/blocks.ttf", 10, 10, font_size=42))
        self.adventure.game.infos.append(
            Label(f'Zombies: {len(self.adventure.zombies)}', "assets/fonts/pixel_square.ttf", 10, 80, font_size=24))

    def finish(self):
        return len(self.adventure.zombies) == 0

    @staticmethod
    def is_end():
        return True
