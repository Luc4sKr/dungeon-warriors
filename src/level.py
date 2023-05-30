import pygame

from .config import *
from .spritesheet import Spritesheet
from .animation import Animation
from .player import Player
from .tilemap import Tilemap
from .camera import Camera


class Level:
    def __init__(self, game, level: str) -> None:
        self.game = game
        self.level = level

        self.map = Tilemap(self)

        player_idle_spritesheet = Spritesheet("assets/sprites/warrior/idle", 240, SCALE)
        player_run_spritesheet = Spritesheet("assets/sprites/warrior/run", 100, SCALE)
        
        player_anim = Animation()
        player_anim.add(PLAYER_IDLE, player_idle_spritesheet)
        player_anim.add(PLAYER_RUN, player_run_spritesheet)
        self.player = Player(player_anim, 5, PLAYER_IMAGE_PATH, (100, 100), scale=SCALE)

        self.camera = Camera(self.player, WIDTH, HEIGHT)

        self.map.all_sprites.add(self.player)

    def update(self):
        tst = pygame.sprite.spritecollide(self.player, self.map.wall_sprites, False, pygame.sprite.collide_mask)
        if tst:
            pass

        self.camera.scroll()
        self.map.update()
        self.map.all_sprites.update()

    def draw(self):
        self.map.draw(self.game.screen)
        
        for sprite in self.map.all_sprites:
            self.game.screen.blit(sprite.image, (sprite.rect.topleft + self.camera.offset))
