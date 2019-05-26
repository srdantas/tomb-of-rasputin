from pygame import Rect
from pygame.sprite import Sprite


class Obstacle(Sprite):
    def __init__(self, game, groups, x, y, w, h):
        Sprite.__init__(self, groups)
        self.game = game
        self.rect = Rect(x, y, w, h)
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
