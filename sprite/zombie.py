from settings import ZOMBIE_BASE_PATH, DIRECTION_RIGHT, DIRECTION_LEFT, DIRECTION_FRONT, DIRECTION_BACK, MOVE_SPEED
from sprite import animation_sprite


class Zombie(animation_sprite.AnimationSprite):

    def __init__(self, game, groups, x, y):
        super().__init__(game, ZOMBIE_BASE_PATH, x, y, groups)

    def update(self):
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

    def _get_distance_player_x(self):
        return self.x - self.game.level.player.x

    def _get_distance_player_y(self):
        return self.y - self.game.level.player.y
