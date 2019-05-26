from pygame import Rect, font

from settings import WHITE


class Label:

    def __init__(self, text, font_file, x, y, font_size=30, color=WHITE):
        self.font = font.Font(font_file, font_size)
        self.surface = self.font.render(text, True, color)
        self.rect = Rect((x, y), self.font.size(text))
