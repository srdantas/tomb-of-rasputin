from pygame import Surface
from pygame.sprite import Sprite, spritecollideany

from settings import ATTACK_SPEED, DIRECTION_BACK, DIRECTION_FRONT, DIRECTION_RIGHT, DIRECTION_LEFT, RED


class Bullet(Sprite):

    def __init__(self, game, x, y, direction, groups):
        self.game = game
        Sprite.__init__(self, groups)

        self.x = x
        self.y = y
        self.direction = direction

        self.image = Surface((5, 5))
        self.image.fill(RED)
        self.rect = self.image.get_rect()

    def update(self):
        if self.direction == DIRECTION_BACK:
            self.y -= ATTACK_SPEED
        elif self.direction == DIRECTION_FRONT:
            self.y += ATTACK_SPEED
        elif self.direction == DIRECTION_LEFT:
            self.x -= ATTACK_SPEED
        elif self.direction == DIRECTION_RIGHT:
            self.x += ATTACK_SPEED

        self.rect.x = self.x
        self.rect.y = self.y

        if spritecollideany(self, self.game.level.walls, False):
            self.kill()
