import pyganim
from pygame import K_LEFT, K_RIGHT, K_UP, K_DOWN, key

from settings import MOVE_SPEED, TILE_SIZE, DIRECTION_FRONT, DIRECTION_BACK, DIRECTION_LEFT, DIRECTION_RIGHT, \
    PLAYER_BASE_PATH
from game.sprite import animation_sprite


def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)


def get_animation_sheet(file, rows=1, cols=1):
    images = pyganim.getImagesFromSpriteSheet(file, rows=rows, cols=cols, rects=[[TILE_SIZE] * 2 + [47, 60]])
    frames = list(zip(images, [1] + ([100] * len(images))))
    return pyganim.PygAnimation(frames)


class Player(animation_sprite.AnimationSprite):
    def __init__(self, game, x, y):
        super().__init__(game, PLAYER_BASE_PATH, x, y, game.all_sprites)

    def update(self):
        self._get_keys()
        self._update_rect()
        self._update_animation()

    def _get_keys(self):
        press = key.get_pressed()
        if press[K_LEFT]:
            self.direction = DIRECTION_LEFT
            self.speed_x -= MOVE_SPEED
        elif press[K_RIGHT]:
            self.direction = DIRECTION_RIGHT
            self.speed_x += MOVE_SPEED
        elif press[K_UP]:
            self.direction = DIRECTION_BACK
            self.speed_y -= MOVE_SPEED
        elif press[K_DOWN]:
            self.direction = DIRECTION_FRONT
            self.speed_y += MOVE_SPEED

        if self.speed_x != 0 or self.speed_y != 0:
            self.is_walk = True
        else:
            self.is_walk = False
