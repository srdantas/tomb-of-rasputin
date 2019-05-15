from pygame import transform, K_LEFT, K_RIGHT, K_UP, K_DOWN, Vector2, Surface, key, sprite

from settings import PLAYER_SPEED, PLAYER_ROT_SPEED, PLAYER_HIT_RECT, TILE_SIZE


def collide_hit_rect(one, two):
    return one.hit_rect.colliderect(two.rect)


class Player(sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        sprite.Sprite.__init__(self, self.groups)
        self.game = game

        self.image = Surface((TILE_SIZE, TILE_SIZE))

        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center

        self.vel = Vector2(0, 0)
        self.pos = Vector2(x, y) * TILE_SIZE
        self.rot = 0

    def _get_keys(self):
        self.rot_speed = 0
        self.vel = Vector2(0, 0)
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rot_speed = PLAYER_ROT_SPEED
        if keys[K_RIGHT]:
            self.rot_speed = -PLAYER_ROT_SPEED
        if keys[K_UP]:
            self.vel = Vector2(PLAYER_SPEED, 0).rotate(-self.rot)
        if keys[K_DOWN]:
            self.vel = Vector2(-PLAYER_SPEED / 2, 0).rotate(-self.rot)

    def _collision_with_wall(self, direction):
        if direction == 'x':
            hits = sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.hit_rect.width / 2.0
                if self.vel.x < 0:
                    self.pos.x = hits[0].rect.right + self.hit_rect.width / 2.0
                self.vel.x = 0
                self.hit_rect.centerx = self.pos.x
        if direction == 'y':
            hits = sprite.spritecollide(self, self.game.walls, False, collide_hit_rect)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.hit_rect.height / 2.0
                if self.vel.y < 0:
                    self.pos.y = hits[0].rect.bottom + self.hit_rect.height / 2.0
                self.vel.y = 0
                self.hit_rect.centery = self.pos.y

    def update(self):
        self._get_keys()

        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360

        self.image = transform.rotate(self.game.player_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        self._collision_with_wall('x')

        self.hit_rect.centery = self.pos.y
        self._collision_with_wall('y')
        self.rect.center = self.hit_rect.center
