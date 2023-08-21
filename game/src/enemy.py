import pygame

from .constants import *
from .entity import AnimatedEntity


class Enemy(AnimatedEntity):
    def __init__(self, game, animation, image_path, pos: tuple, speed, life, scale=SCALE) -> None:
        super().__init__(game, animation, image_path, pos, speed, life, scale)

        self.game = game

        self.damage = 10
        self.speed = speed
        self.direction = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(pos)

        self.rect.x = self.pos.x
        self.rect.bottom = self.pos.y + (self.image.get_height() / 2)

        self.is_running = False
        self.invert_sprite = False

        self.time = 0
        self.attack_cooldown = 350
        self.attacking = False

    def animation_control(self):
        self.animation.select(ENEMY_IDLE)

    def update(self):
        self.animation_control()