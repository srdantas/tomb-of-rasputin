import sys

from game.camera import Camera
from game.tilemap import TiledMap
from settings import *
from sprite.player import Player
from sprite.obstacle import Obstacle
from sprite.zombie import Zombie
from game.home import Home


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

        self.level = Home(self)

        self.camera = Camera(self.level.map.width, self.level.map.height)

    def run(self):
        self.playing = True

        while self.playing:
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.all_sprites.update()
        self.camera.update(self.level.player)

    def draw(self):
        self.screen.blit(self.level.map_image, self.camera.apply_rect(self.level.map_rect))

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
