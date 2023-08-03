import pygame
import math

from .constants import *

class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, image, damage, scale=SCALE):
        super().__init__()
        self.player = player

        self.image = pygame.image.load(f"assets/sprites/weapons/{image}.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))
        self.base_image = self.image
        self.rect = self.image.get_rect()

        self.offset = pygame.math.Vector2(0, -50)
        self.offset_rotated = pygame.math.Vector2(0, -25)

        self.rect.center = self.player.rect.center

    def rotate(self):
        mx, my = pygame.mouse.get_pos()
        dx = mx - self.player.rect.centerx  # - 64
        dy = my - self.player.rect.centery  # - 32

        self.angle = (180 / math.pi) * math.atan2(dy, dx)

        position = self.player.rect.center
        offset_rotated = self.offset.rotate(-self.angle)
        self.rect = self.image.get_rect(center=position + offset_rotated)
        #self.rect = pygame.mask.from_surface(self.image)
        self.offset_rotated = pygame.math.Vector2(0, -35).rotate(-self.angle)

        self.image = pygame.transform.rotate(self.base_image, self.angle)


    def update(self):
        self.rect.center = self.player.rect.center

        self.rotate()