import sys

from pygame import QUIT, KEYDOWN, K_ESCAPE, display, quit, time, init, key, font
from pygame import event as key_event
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

        self.labels = list()

        self.all_sprites = Group()

        self.level = Home(self)

        self.camera = Camera(self.level.map.width, self.level.map.height)

    def update_level(self, level):
        self.labels = list()

        self.level.player.kill()

        self.level = level
        self._update_camera()

        self.update()
        self.draw()

    def run(self):
        self.playing = True

        while self.playing:
            self.events()
            self.update()
            if not self.level.has_menu:
                self.draw()

    def update(self):
        self.level.update()
        self.all_sprites.update()
        self.camera.update(self.level.player)

    def draw(self):
        self.screen.blit(self.level.map_image, self.camera.apply_rect(self.level.map_rect))

        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        for label in self.labels:
            self.screen.blit(label.surface, self.camera.apply_rect(label.rect))

        display.flip()

    def events(self):
        events = key_event.get()
        if not self.level.has_menu:
            for event in events:
                if event.type == QUIT:
                    self.__quit__()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.__quit__()

        self.level.events(events)

    def show_start_screen(self):
        pass

    def show_go_screen(self):
        pass

    def _update_camera(self):
        self.camera = Camera(self.level.map.width, self.level.map.height)

    @staticmethod
    def __quit__():
        quit()
        sys.exit()
