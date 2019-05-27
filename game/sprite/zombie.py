from pygame import Rect, draw
from pygame.sprite import spritecollideany

from game.sprite import animation_sprite
from settings import ZOMBIE_BASE_PATH, DIRECTION_RIGHT, DIRECTION_LEFT, DIRECTION_FRONT, DIRECTION_BACK, MOVE_SPEED, \
    ZOMBIE_HEALTH, ATTACK_DAMAGE, GREEN


class Zombie(animation_sprite.AnimationSprite):

    def __init__(self, game, groups, x, y):
        super().__init__(game, ZOMBIE_BASE_PATH, x, y, groups)

        self.health = ZOMBIE_HEALTH

    def update(self):
        self._update_health()
        self._get_player()
        self._update_rect()
        self._update_animation()

    def _get_player(self):
        distance_x = self._get_distance_player_x()
        distance_y = self._get_distance_player_y()

        if abs(distance_x) >= abs(distance_y):
            if distance_x < 0:
                self.direction = DIRECTION_RIGHT
                self.speed_x += MOVE_SPEED / 2
            elif distance_x > 0:
                self.direction = DIRECTION_LEFT
                self.speed_x -= MOVE_SPEED / 2
        else:
            if distance_y < 0:
                self.direction = DIRECTION_FRONT
                self.speed_y += MOVE_SPEED / 2
            elif distance_y > 0:
                self.direction = DIRECTION_BACK
                self.speed_y -= MOVE_SPEED / 2

        if self.speed_x != 0 or self.speed_y != 0:
            self.is_walk = True
        else:
            self.is_walk = False

    def draw_health(self):
        width = int(self.rect.width * self.health / ZOMBIE_HEALTH)
        health_bar = Rect(0, 0, width, 5)
        if self.health < ZOMBIE_HEALTH:
            draw.rect(self.image, GREEN, health_bar)

    def _update_health(self):
        hit = spritecollideany(self, self.game.level.bullets, False)
        if hit:
            self.health -= ATTACK_DAMAGE
            hit.kill()

        if self.health <= 0:
            self.kill()

    def _get_distance_player_x(self):
        return self.x - self.game.level.player.x

    def _get_distance_player_y(self):
        return self.y - self.game.level.player.y
