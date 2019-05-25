import sys

from game.camera import Camera
from game.tilemap import TiledMap
from settings import *
from sprite.player import Player
from sprite.wall import Obstacle
from sprite.zombie import Zombie


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(TITLE)
        pg.key.set_repeat()

        self.playing = False

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))

        self.clock = pg.time.Clock()
        self.dt = self.clock.tick(FPS) / 1000

        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.zombies = pg.sprite.Group()

        self.map = TiledMap('maps/tiled1.tmx')
        self.map_image = self.map.make_map()
        self.map_rect = self.map_image.get_rect()

        for tile_object in self.map.tiled_map.objects:
            if tile_object.name == 'player':
                self.player = Player(self, tile_object.x * self.map.scale, tile_object.y * self.map.scale)
            if tile_object.name == 'wall':
                Obstacle(self,
                         tile_object.x * self.map.scale,
                         tile_object.y * self.map.scale,
                         tile_object.width * self.map.scale,
                         tile_object.height * self.map.scale)
            if tile_object.name == 'zombie':
                Zombie(self, tile_object.x * self.map.scale, tile_object.y * self.map.scale)

        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        self.playing = True

        while self.playing:
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw(self):
        self.screen.blit(self.map_image, self.camera.apply_rect(self.map_rect))

        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        pg.display.flip()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.__quit__()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.__quit__()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

    @staticmethod
    def __quit__():
        pg.quit()
        sys.exit()
