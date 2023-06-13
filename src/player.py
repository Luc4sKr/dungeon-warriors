import pygame

from .config import *
from .utils import get_mask_rect
from .object import AnimatedObject
from .weapon import Bow

class Player(AnimatedObject):
    def __init__(self, level, animation, speed, image, pos: tuple, wall_sprites, scale=1) -> None:
        super().__init__(animation, image, pos, scale)

        self.speed = speed
        self.wall_sprites = wall_sprites
        self.level = level
        
        self.weapon = Bow(f"{WEAPONS_PATH}/bow/unarmed.png", self.rect.center, scale=2)

        self.hitbox = get_mask_rect(self.image, *self.rect.topleft)

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

        self.hitbox = get_mask_rect(self.image, *self.rect.topleft)

        self.pos.x += self.direction.x * self.speed
        self.pos.y += self.direction.y * self.speed

        self.wall_collision()
        self.rect.center = self.pos

    def wall_collision(self):
        test_rect = self.hitbox.move(self.direction.x * self.speed, self.direction.y * self.speed)
        collide_points = (test_rect.midbottom, test_rect.bottomleft, test_rect.bottomright)
        for wall in self.level.map.wall_sprites:
            if any(wall.rect.collidepoint(point) for point in collide_points):
                self.speed = 0
            else: 
                self.speed = 5
            
        print(f"{self.rect.center}, {test_rect.center}")

    def animation_control(self):
        self.animation.select(PLAYER_IDLE)
        if self.is_running:
            self.animation.select(PLAYER_RUN)

        self.image = self.animation.update_animation()
        self.image = pygame.transform.flip(self.image, self.invert_sprite, False)

    def update(self):
        self.input()
        self.animation_control()

