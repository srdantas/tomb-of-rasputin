import sys

from pygame import QUIT, KEYDOWN, K_ESCAPE
from pygame import display, quit
from pygame import event as key_event
from pygame import time, init, key, font
from pygame.sprite import Group

from game.camera import Camera
from game.home import Home
from settings import *


class Game:
    def __init__(self):
        init()
        font.init()
        display.set_caption(TITLE)
        key.set_repeat()

        self.playing = False

        self.screen = display.set_mode((WIDTH, HEIGHT))

        self.clock = time.Clock()
        self.dt = self.clock.tick(FPS) / 1000

        # self.font = font.Font('Comic Sans MS', 30)

        self.all_sprites = Group()

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

        display.flip()

    def events(self):
        for event in key_event.get():
            if event.type == QUIT:
                self.__quit__()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.__quit__()

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

    @staticmethod
    def __quit__():
        quit()
        sys.exit()
