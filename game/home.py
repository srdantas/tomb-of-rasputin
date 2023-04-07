import pygame_menu
from pygame import QUIT, K_ESCAPE, KEYDOWN, K_SPACE
from pygame.sprite import Group
from pygame.sprite import spritecollide, collide_circle

from adventures import adventures
from game.label import Label
from game.sprite.obstacle import Obstacle
from game.sprite.player import Player
from game.tilemap import TiledMap
from settings import DARKGREY, WIDTH, HEIGHT


class Home:
    def __init__(self, game):
        self.game = game
        self.walls = Group()
        self.bullets = Group()
        self.zombies = Group()
        self.adventurers = Group()

        self.finish = False

        self.adventures_menu = pygame_menu
        .Menu(game.screen, WIDTH, HEIGHT, 'assets/fonts/blocks.ttf',
                                               "Adventures", dopause=False)
        self._close_menu()

        self._create_list_adventures()

        self.map = TiledMap('assets/maps/home.tmx')
        self.map_image = self.map.make_map()
        self.map_rect = self.map_image.get_rect()

        for tile_object in self.map.tiled_map.objects:
            if tile_object.name == 'wall':
                self._create_obstacle(tile_object, self.walls)
            elif tile_object.name == 'adventurer':
                self.adventurer = self._create_adventurer(game, tile_object)
            elif tile_object.name == 'ranking':
                self._create_ranker(tile_object)
            elif tile_object.name == 'player':
                self._create_player(tile_object)

    def update(self):
        self._info()
        collisions = spritecollide(self.player, self.adventurers, False, collide_circle)
        if collisions:
            self.adventures_menu.enable()

    def events(self, events):
        if self.adventures_menu.is_enabled() and self.has_menu:
            self._list_adventures(events)

        for event in events:
            if event.type == QUIT:
                self._close_menu()

            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self._show_menu()

                elif event.key == K_ESCAPE:
                    self._close_menu()

    def _close_menu(self):
        self.adventures_menu.disable()
        self.has_menu = False

    def _show_menu(self):
        if self.adventures_menu.is_enabled():
            self.has_menu = True

    def _create_list_adventures(self):
        for adventure in adventures.adventures(self.game):
            self.adventures_menu.add_option(adventure['name'], adventure['adventure'].execute)

    def _list_adventures(self, events):
        self.adventures_menu.mainloop(events)

    def _create_player(self, tile_object):
        self.player = Player(self.game, tile_object.x * self.map.scale, tile_object.y * self.map.scale)

    def _create_adventurer(self, game, tile_object):
        game.labels.append(
            Label('Adventurer', 'assets/fonts/pixel_square.ttf', (tile_object.x - tile_object.width) * self.map.scale,
                  (tile_object.y + tile_object.height) * self.map.scale, font_size=16, color=DARKGREY))
        self._create_obstacle(tile_object, self.walls)
        return self._create_obstacle(tile_object, self.adventurers)

    def _create_ranker(self, tile_object):
        self.game.labels.append(
            Label('Ranking', 'assets/fonts/pixel_square.ttf', (tile_object.x - tile_object.width) * self.map.scale,
                  tile_object.y * self.map.scale, font_size=16, color=DARKGREY))
        self._create_obstacle(tile_object, self.walls)

    def _create_obstacle(self, tile_object, group):
        return Obstacle(self.game,
                        group,
                        tile_object.x * self.map.scale,
                        tile_object.y * self.map.scale,
                        tile_object.width * self.map.scale,
                        tile_object.height * self.map.scale)

    def _info(self):
        self.game.infos.append(Label('Home', "assets/fonts/blocks.ttf", 10, 10, font_size=42))
        self.game.infos.append(
            Label('Select a adventure for play it', "assets/fonts/future_narrow.ttf", 10, 80, font_size=16))
