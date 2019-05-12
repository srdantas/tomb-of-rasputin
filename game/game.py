import sys

import pygame as pg

from game.camera import Camera
from game.sprites import Player
from game.tilemap import Map
from settings import *


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption(TITLE)
        pg.key.set_repeat()

        self.screen = pg.display.set_mode((WIDTH, HEIGHT))

        self.clock = pg.time.Clock()
        self.dt = self.clock.tick(FPS) / 1000

        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()

        self.player = Player(self, 10, 10)

        self.playing = False

        self.map = Map('maps/map.txt')
        self.camera = Camera(self.map.width, self.map.height)

    @staticmethod
    def quit():
        pg.quit()
        sys.exit()

    def run(self):
        self.playing = True

        self.map.load(self)

        while self.playing:
            self.events()
            self.update()
            self.draw()

    def update(self):
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
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass
