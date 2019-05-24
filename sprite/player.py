import pyganim
from pygame import K_LEFT, K_RIGHT, K_UP, K_DOWN, sprite, key

from settings import PLAYER_SPEED, TILE_SIZE, PLAYER_FRONT_STOP, PLAYER_FRONT_WALK, PLAYER_BACK_WALK, PLAYER_BACK_STOP, \
    PLAYER_LEFT_WALK, PLAYER_LEFT_STOP, PLAYER_RIGHT_WALK, PLAYER_RIGHT_STOP, DIRECTION_FRONT, DIRECTION_BACK, \
    DIRECTION_LEFT, DIRECTION_RIGHT


def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)


def get_animation_sheet(file, rows=1, cols=1):
    images = pyganim.getImagesFromSpriteSheet(file, rows=rows, cols=cols, rects=[[TILE_SIZE] * 4])
    frames = list(zip(images, [1] + ([100] * len(images))))
    return pyganim.PygAnimation(frames)


class Player(sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.player_front_walk = get_animation_sheet(PLAYER_FRONT_WALK, cols=9)
        self.player_front_stop = get_animation_sheet(PLAYER_FRONT_STOP)

        self.player_back_walk = get_animation_sheet(PLAYER_BACK_WALK, cols=9)
        self.player_back_stop = get_animation_sheet(PLAYER_BACK_STOP)

        self.player_left_walk = get_animation_sheet(PLAYER_LEFT_WALK, cols=9)
        self.player_left_stop = get_animation_sheet(PLAYER_LEFT_STOP)

        self.player_right_walk = get_animation_sheet(PLAYER_RIGHT_WALK, cols=9)
        self.player_right_stop = get_animation_sheet(PLAYER_RIGHT_STOP)

        self.image = self.player_front_stop.getCurrentFrame()
        self.rect = self.image.get_rect()

        self.direction = DIRECTION_FRONT
        self.is_walk = False

        self._reset_speed()

        self.x = x
        self.y = y

        self.player_front_walk.play()
        self.player_front_stop.play()

        self.player_back_walk.play()
        self.player_back_stop.play()

        self.player_left_walk.play()
        self.player_left_stop.play()

        self.player_right_walk.play()
        self.player_right_stop.play()

    def update(self):
        self._get_keys()

        self._update_rect()

        self._update_animation()

    def _update_animation(self):
        if self.direction == DIRECTION_BACK:
            if self.is_walk:
                self.image = self.player_back_walk.getCurrentFrame()
            else:
                self.image = self.player_back_stop.getCurrentFrame()

        elif self.direction == DIRECTION_FRONT:
            if self.is_walk:
                self.image = self.player_front_walk.getCurrentFrame()
            else:
                self.image = self.player_front_stop.getCurrentFrame()

        elif self.direction == DIRECTION_LEFT:
            if self.is_walk:
                self.image = self.player_left_walk.getCurrentFrame()
            else:
                self.image = self.player_left_stop.getCurrentFrame()

        elif self.direction == DIRECTION_RIGHT:
            if self.is_walk:
                self.image = self.player_right_walk.getCurrentFrame()
            else:
                self.image = self.player_right_stop.getCurrentFrame()

    def _update_rect(self):
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
            self.direction = DIRECTION_LEFT
            self.speed_x -= PLAYER_SPEED
        elif press[K_RIGHT]:
            self.direction = DIRECTION_RIGHT
            self.speed_x += PLAYER_SPEED
        elif press[K_UP]:
            self.direction = DIRECTION_BACK
            self.speed_y -= PLAYER_SPEED
        elif press[K_DOWN]:
            self.direction = DIRECTION_FRONT
            self.speed_y += PLAYER_SPEED

        if self.speed_x != 0 or self.speed_y != 0:
            self.is_walk = True
        else:
            self.is_walk = False

    def _reset_speed(self):
        self.speed_x, self.speed_y = 0, 0
