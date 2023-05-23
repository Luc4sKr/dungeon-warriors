import pygame

from .config import *
from .object import Object
from .image import Image
from .animation import Animation

class Player(Object):
    def __init__(self, image: Image, pos_x, pos_y, health, scale=1, rotation=0) -> None:
        super().__init__(pos_x, pos_y, health, scale, rotation)
    
        self.player_img = image

        self.image = self.player_img.image
        self.rect = self.image.get_rect()
        self.rect.center = (HALF_WIDTH, HALF_HEIGHT)

        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        self.anim = Animation(WARRIOR_IDLE_PATH, 180)

    def update_animation(self):
        self.image = self.anim.animation[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > self.anim.delay:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.anim.animation):
            self.frame_index = 0


    def update(self):
        self.update_animation()
