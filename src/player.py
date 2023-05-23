import pygame
from math import sqrt, sin, cos

from .config import *
from .object import Object
from .image import Image
from .animation import Animation
from .spritesheet import Spritesheet

class Player(Object):
    def __init__(self, image: Image, animation: Animation, pos_x, pos_y, health) -> None:
        super().__init__(pos_x, pos_y, health)
    
        self.player_img = image
        self.animation = animation

        self.image = self.player_img.image
        self.rect = self.image.get_rect()
        self.rect.center = (HALF_WIDTH, HALF_HEIGHT)

        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

        self.animation.select(PLAYER_IDLE)

    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            pass
        if keys[pygame.K_s]:
            pass
        if keys[pygame.K_d]:
            pass
        if keys[pygame.K_a]:
            pass
        
    def update(self):
        self.movement()
        self.image = self.animation.update_animation()
