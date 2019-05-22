import pyganim
from pygame import K_LEFT, K_RIGHT, K_UP, K_DOWN, sprite, key

from settings import PLAYER_SPEED, TILE_SIZE, PLAYER_IMG


def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)


class Player(sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.images = pyganim.getImagesFromSpriteSheet(PLAYER_IMG, rows=1, cols=6,
                                                       rects=[[TILE_SIZE, TILE_SIZE, TILE_SIZE, TILE_SIZE]])
        self.frames = list(zip(self.images, [80, 80, 80, 80, 80, 80]))
        self.animation_object = pyganim.PygAnimation(self.frames)

        self.image = self.animation_object.getCurrentFrame()
        self.rect = self.image.get_rect()

        self.animation_object.play()

        self._reset_speed()

        self.x = x
        self.y = y

    def update(self):
        self._get_keys()

        self._update_move()

        self.image = self.animation_object.getCurrentFrame()

    def _update_move(self):
        self._make_collision_with_walls()

        self.x += self.speed_x
        self.y += self.speed_y
        self._reset_speed()

        self.rect.x = self.x
        self.rect.y = self.y

    def _make_collision_with_walls(self):
        hits = sprite.spritecollide(self, self.game.walls, False)
        if hits:
            if self.speed_y > 0:
                self.y = hits[0].rect.top - self.rect.height
            if self.speed_y < 0:
                self.y = hits[0].rect.bottom

            if self.speed_x > 0:
                self.x = hits[0].rect.left - self.rect.width
            if self.speed_x < 0:
                self.x = hits[0].rect.right

            self._reset_speed()

            self.rect.y = self.y
            self.rect.x = self.x

    def _get_keys(self):
        press = key.get_pressed()
        if press[K_LEFT]:
            self.speed_x -= PLAYER_SPEED
        elif press[K_RIGHT]:
            self.speed_x += PLAYER_SPEED
        elif press[K_UP]:
            self.speed_y -= PLAYER_SPEED
        elif press[K_DOWN]:
            self.speed_y += PLAYER_SPEED

    def _reset_speed(self):
        self.speed_x, self.speed_y = 0, 0
