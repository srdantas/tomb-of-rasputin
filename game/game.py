import sys
import time as sys_timer

from pygame import QUIT, KEYDOWN, K_ESCAPE, display, quit, time, init, key, font, Surface
from pygame import event as key_event
from pygame.sprite import Group

from game.camera import Camera
from game.home import Home
from game.label import Label
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
        self.infos = list()

        self.all_sprites = Group()

        self.level = Home(self)

        self.camera = Camera(self.level.map.width, self.level.map.height)

        self.game_over = False

    def update_level(self, level):
        self.level.player.kill()
        self.labels = list()
        self.infos = list()

        self.level = level
        self._update_camera()

    def run(self):
        self.playing = True

        while self.playing:
            self.events()
            self.update()
            if not self.level.has_menu:
                self.draw()

            if self.game_over:
                break

    def update(self):
        # update info
        self.infos = list()

        self.level.update()
        self.all_sprites.update()
        self.camera.update(self.level.player)

    def draw(self):
        self.screen.blit(self.level.map_image, self.camera.apply_rect(self.level.map_rect))

        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))

        for label in self.labels:
            self.screen.blit(label.surface, self.camera.apply_rect(label.rect))

        for info in self.infos:
            self.screen.blit(info.surface, info.rect)

        for zombie in self.level.zombies:
            zombie.draw_health()

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

    def game_over_screen(self):
        game_over_display = Surface((WIDTH, HEIGHT))
        game_over_display.fill(BLACK)
        game_over_text = Label('Game Over', "assets/fonts/blocks.ttf", 20, (HEIGHT / 2) - 100, font_size=72)
        score_text = Label('For save the score you need finish adventure', "assets/fonts/future_narrow.ttf", 20,
                           (HEIGHT / 2) - 120, font_size=24)
        self.screen.blit(game_over_display, (0, 0))
        self.screen.blit(game_over_text.surface, game_over_text.rect)
        self.screen.blit(score_text.surface, score_text.rect)

        display.flip()

        sys_timer.sleep(10)

    def _update_camera(self):
        self.camera = Camera(self.level.map.width, self.level.map.height)

    @staticmethod
    def __quit__():
        quit()
        sys.exit()
