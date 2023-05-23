import pygame

from .config import *
from .image import Image
from .spritesheet import Spritesheet
from .animation import Animation
from .player import Player

class ObjectHandler:
    def __init__(self, game) -> None:
        self.game = game

        self.spite_list = pygame.sprite.Group()

        player_img = Image("assets\sprites\warrior\idle\sprite-1.png", SCALE)
        player_idle_spritesheet = Spritesheet("assets\\sprites\\warrior\\idle", 240, SCALE)
        player_run_spritesheet = Spritesheet("assets\\sprites\\warrior\\run", 100, SCALE)

        player_anim = Animation()
        player_anim.add(1, player_idle_spritesheet)
        player_anim.add(2, player_run_spritesheet)

        self.player = Player(player_img, player_anim, 100, 100)
        self.player_group = pygame.sprite.GroupSingle(self.player)

        self.add_sprite(self.player)



        self.load_images()

    def update(self):
        self.spite_list.update()
    
    def draw(self):
        self.spite_list.draw(self.game.screen)
        self.player_group.draw(self.game.screen)

    def add_sprite(self, sprite):
        self.spite_list.add(sprite)

    def load_images(self):
        self.TILE_FLOOR_1 = Image(f"{TILESETS_PATH}\\floor\\1.png", scale=SCALE)