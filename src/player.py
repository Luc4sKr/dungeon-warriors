import pygame

from .constants import *
from .entity import AnimatedEntity

class Player(AnimatedEntity):
    def __init__(self, game, animation, speed, image, pos: tuple, scale=1) -> None:
        super().__init__(game, animation, image, pos, speed, scale)

        self.game = game

        self.speed = speed

        self.direction = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(pos)

        self.is_running = False
        self.invert_sprite = False

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_d]:
            self.direction.x = 1
            self.invert_sprite = False
        elif keys[pygame.K_a]:
            self.direction.x = -1
            self.invert_sprite = True
        else:
            self.direction.x = 0

        self.move()

    def move(self):
        self.is_running = False
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            self.is_running = True

        self.rect.x += self.direction.x * self.speed
        super().wall_collision("horizontal")

        self.rect.y += self.direction.y * self.speed
        super().wall_collision("vertical")


    def animation_control(self):
        self.animation.select(PLAYER_IDLE)
        if self.is_running:
            self.animation.select(PLAYER_RUN)

        self.image = self.animation.update_animation()
        self.image = pygame.transform.flip(self.image, self.invert_sprite, False)


    def update(self):
        self.input()
        self.animation_control()
