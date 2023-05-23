from .image import Image

RESOLUTION = WIDTH, HEIGHT = 854, 480
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

FPS = 60
SCALE = 3

# PATH's
SPRITES_PATH = "assets\\sprites"
TILESETS_PATH = "assets\\tilesets"
LEVELS_PATH = "assets\\levels"

WARRIOR_IDLE_PATH = f"{SPRITES_PATH}\\warrior\\idle"

# PLAYER
PLAYER_IDLE = 1
PLAYER_RUN = 2
PLAYER_HIT = 3

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
DARKGRAY = (50, 50, 50)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)