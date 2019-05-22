import sys

from game.camera import Camera
from game.tilemap import Map
from settings import *
from sprite.player import Player


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

        self.player = Player(self, 100, 100)

        self.map = Map('maps/map.txt')
        self.camera = Camera(self.map.width, self.map.height)

    def run(self):
        self.playing = True

        self.map.load(self)

        while self.playing:
            self.events()
            self.update()
            self.draw()

    def update(self):
        self.player.update()
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        for x in range(0, WIDTH, TILE_SIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILE_SIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.draw_grid()

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
