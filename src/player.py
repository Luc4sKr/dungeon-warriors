import pygame

from .config import *
from .object import AnimatedObject
from .weapon import Bow

class Player(AnimatedObject):
    def __init__(self, animation, speed, image, pos: tuple, wall_sprites, scale=1) -> None:
        super().__init__(animation, image, pos, scale)

        self.speed = speed
        self.wall_sprites = wall_sprites
        
        self.weapon = Bow(f"{WEAPONS_PATH}/bow/unarmed.png", self.rect.center, scale=2)

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

        self.pos.x += self.direction.x * self.speed
        self.collision("horizontal")

        self.pos.y += self.direction.y * self.speed
        self.collision("vertical")

        self.rect.center = self.pos

    def collision(self, direction):
        if direction == 'horizontal':
            for sprite in self.wall_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0: # moving right
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0: # moving left
                        self.rect.left = sprite.rect.right

        if direction == 'vertical':
            for sprite in self.wall_sprites:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0: # moving down
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0: # moving up
                        self.rect.top = sprite.rect.bottom

    def animation_control(self):
        self.animation.select(PLAYER_IDLE)
        if self.is_running:
            self.animation.select(PLAYER_RUN)

        self.image = self.animation.update_animation()
        self.image = pygame.transform.flip(self.image, self.invert_sprite, False)


    def update(self):
        self.input()
        self.animation_control()


        self.weapon.rect.x = self.rect.x
        self.weapon.rect.y = self.rect.y
