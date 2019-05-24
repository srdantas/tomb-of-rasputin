import pygame as pg

# define some constants
DIRECTION_FRONT = 'front'
DIRECTION_BACK = 'back'
DIRECTION_LEFT = 'left'
DIRECTION_RIGHT = 'right'

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = "Tomb of Rasputin"
BACKGROUND_COLOR = DARKGREY

TILE_SIZE = 60
GRID_WIDTH = WIDTH / TILE_SIZE
GRID_HEIGHT = HEIGHT / TILE_SIZE

PLAYER_HIT_RECT = pg.Rect(0, 0, TILE_SIZE, TILE_SIZE)
PLAYER_SPEED = .1

PLAYER_FRONT_STOP = 'image/player/front/front_stop.png'
PLAYER_FRONT_WALK = 'image/player/front/front_walk.png'

PLAYER_BACK_STOP = 'image/player/back/back_stop.png'
PLAYER_BACK_WALK = 'image/player/back/back_walk.png'

PLAYER_LEFT_STOP = 'image/player/left/left_stop.png'
PLAYER_LEFT_WALK = 'image/player/left/left_walk.png'

PLAYER_RIGHT_STOP = 'image/player/right/right_stop.png'
PLAYER_RIGHT_WALK = 'image/player/right/right_walk.png'
