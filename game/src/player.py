import pygame

from .utils import *
from .constants import *

from .entity import AnimatedEntity
from .weapon import Weapon


class Player(AnimatedEntity):
    def __init__(self, obj_handler, animation, model, image, pos: tuple, scale=SCALE) -> None:
        super().__init__(obj_handler, animation, image, pos, speed=model.speed, life=model.life, scale=scale)

        self.obj_handler = obj_handler
        self.model = model

        self.weapon = Weapon(self.obj_handler, self, self.model.weapon.name, self.model.weapon.damage)
        self.obj_handler.weapon_group.add(self.weapon)

        self.direction = pygame.math.Vector2(0, 0)
        self.pos = pygame.math.Vector2(pos)

        self.is_running = False
        self.invert_sprite = False

        self.is_invisible = False
        self.invisible_time = pygame.time.get_ticks()
        self.invisible_cooldown = 1000

        self.attacking = False
        self.time_attack = pygame.time.get_ticks()
        self.attack_cooldown = 350

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

        if pygame.mouse.get_pressed()[0] and pygame.time.get_ticks() - self.time_attack > self.attack_cooldown:
            self.time_attack = pygame.time.get_ticks()
            self.attacking = True
            self.weapon.weapon_swing.swing_side *= (-1)

    def move(self):
        self.is_running = False
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            self.is_running = True

        self.rect.x += self.direction.x * self.model.speed
        super().wall_collision("horizontal")

        self.rect.y += self.direction.y * self.model.speed
        super().wall_collision("vertical")

    def animation_control(self):
        self.animation.select(PLAYER_IDLE)
        if self.is_running:
            self.animation.select(PLAYER_RUN)

        self.image = self.animation.update_animation()
        self.image = pygame.transform.flip(self.image, self.invert_sprite, False)

    def enemy_collide(self):
        for enemy in self.obj_handler.enemy_group:
            if pygame.sprite.collide_mask(self, enemy) and not self.is_invisible:
                self.life -= enemy.damage
                self.is_invisible = True

    def invisible_manager(self):
        if pygame.time.get_ticks() - self.invisible_time > self.invisible_cooldown and self.is_invisible:
            self.invisible_time = pygame.time.get_ticks()
            self.is_invisible = False

    def draw_username(self, screen):
        text = return_text(self.model.username, 12, WHITE, self.rect.centerx, self.rect.top)
        screen.blit(text[0], (text[1].topleft + self.obj_handler.camera.offset))

    def update(self):
        self.input()
        self.animation_control()
        self.enemy_collide()
        self.invisible_manager()

