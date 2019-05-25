from os import path

import pyganim
from pygame import sprite

from settings import TILE_SIZE, DIRECTION_FRONT, DIRECTION_BACK, DIRECTION_LEFT, DIRECTION_RIGHT


def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)


def get_animation_sheet(file, rows=1, cols=1):
    images = pyganim.getImagesFromSpriteSheet(file, rows=rows, cols=cols, rects=[[TILE_SIZE] * 2 + [47, 60]])
    frames = list(zip(images, [1] + ([100] * len(images))))
    return pyganim.PygAnimation(frames)


class AnimationSprite(sprite.Sprite):
    def __init__(self, game, images_base_path, x, y, groups):
        self.game = game
        self.images_path = path.join("images", images_base_path)
        self.x = x
        self.y = y
        self.groups = groups

        sprite.Sprite.__init__(self, self.groups)

        self.front_walk = get_animation_sheet(path.join(self.images_path, "front/walk.png"), cols=9)
        self.front_stop = get_animation_sheet(path.join(self.images_path, "front/stop.png"))
        self.front_walk.play()
        self.front_stop.play()

        self.back_walk = get_animation_sheet(path.join(self.images_path, "back/walk.png"), cols=9)
        self.back_stop = get_animation_sheet(path.join(self.images_path, "back/stop.png"))
        self.back_walk.play()
        self.back_stop.play()

        self.left_walk = get_animation_sheet(path.join(self.images_path, "left/walk.png"), cols=9)
        self.left_stop = get_animation_sheet(path.join(self.images_path, "left/stop.png"))
        self.left_walk.play()
        self.left_stop.play()

        self.right_walk = get_animation_sheet(path.join(self.images_path, "right/walk.png"), cols=9)
        self.right_stop = get_animation_sheet(path.join(self.images_path, "right/stop.png"))
        self.right_walk.play()
        self.right_stop.play()

        self.image = self.front_stop.getCurrentFrame()
        self.rect = self.image.get_rect()

        self.direction = DIRECTION_FRONT
        self.is_walk = False

        self._reset_speed()

    def _update_rect(self):
        self.x += self.speed_x
        self.y += self.speed_y

        self.rect.x = self.x
        self.rect.y = self.y

        self._make_collision_with_walls()

        self._reset_speed()

    def _update_animation(self):
        if self.direction == DIRECTION_BACK:
            if self.is_walk:
                self.image = self.back_walk.getCurrentFrame()
            else:
                self.image = self.back_stop.getCurrentFrame()

        elif self.direction == DIRECTION_FRONT:
            if self.is_walk:
                self.image = self.front_walk.getCurrentFrame()
            else:
                self.image = self.front_stop.getCurrentFrame()

        elif self.direction == DIRECTION_LEFT:
            if self.is_walk:
                self.image = self.left_walk.getCurrentFrame()
            else:
                self.image = self.left_stop.getCurrentFrame()

        elif self.direction == DIRECTION_RIGHT:
            if self.is_walk:
                self.image = self.right_walk.getCurrentFrame()
            else:
                self.image = self.right_stop.getCurrentFrame()

    def _make_collision_with_walls(self):
        hits = sprite.spritecollide(self, self.game.walls, False)
        if hits:
            if self.speed_y > 0:
                self.y = hits[0].rect.top - self.rect.height
            elif self.speed_y < 0:
                self.y = hits[0].rect.bottom
            elif self.speed_x > 0:
                self.x = hits[0].rect.left - self.rect.width
            elif self.speed_x < 0:
                self.x = hits[0].rect.right

            self._reset_speed()

            self.rect.y = self.y
            self.rect.x = self.x

    def _reset_speed(self):
        self.speed_x, self.speed_y = 0, 0
