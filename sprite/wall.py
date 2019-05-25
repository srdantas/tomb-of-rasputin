from pygame import Surface, Rect
from pygame.sprite import Sprite

from settings import TILE_SIZE, LIGHTGREY


class Wall(Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        Sprite.__init__(self, self.groups)
        self.game = game
        self.image = Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill(LIGHTGREY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILE_SIZE
        self.rect.y = y * TILE_SIZE


class Obstacle(Sprite):
    def __init__(self, game, x, y, w, h):
        self.groups = game.walls
        Sprite.__init__(self, self.groups)
        self.game = game
        self.rect = Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
