import pygame
import math

from .constants import *
from .utils import get_mask_rect


class WeaponSwing:
    left_swing = 10
    right_swing = -190

    def __init__(self, weapon):
        self.weapon = weapon
        self.angle = 0
        self.offset = pygame.math.Vector2(0, -50)
        self.offset_rotated = pygame.math.Vector2(0, -25)
        self.counter = 0
        self.swing_side = 1

    def reset(self):
        self.counter = 0

    def rotate(self, weapon=None):
        mx, my = pygame.mouse.get_pos()
        dx = mx - self.weapon.player.rect.centerx - self.weapon.player.obj_handler.camera.offset.x
        dy = my - self.weapon.player.rect.centery - self.weapon.player.obj_handler.camera.offset.y

        if self.swing_side == 1:
            self.angle = (180 / math.pi) * math.atan2(-self.swing_side * dy, dx) + self.left_swing
        else:
            self.angle = (180 / math.pi) * math.atan2(self.swing_side * dy, dx) + self.right_swing

        position = self.weapon.player.rect.center
        if weapon:
            self.weapon.image = pygame.transform.rotozoom(self.weapon.image, self.angle, 1)
        else:
            self.weapon.image = pygame.transform.rotozoom(self.weapon.base_image, self.angle, 1)

        offset_rotated = self.offset.rotate(-self.angle)
        self.weapon.rect = self.weapon.image.get_rect(center=position + offset_rotated)
        self.offset_rotated = pygame.math.Vector2(0, -35).rotate(-self.angle)

    def swing(self):
        self.angle += 20 * self.swing_side
        position = self.weapon.player.rect.center
        self.weapon.image = pygame.transform.rotozoom(self.weapon.base_image, self.angle, 1)
        offset_rotated = self.offset.rotate(-self.angle)
        self.weapon.rect = self.weapon.image.get_rect(center=position + offset_rotated)
        self.counter += 1


class Weapon(pygame.sprite.Sprite):
    def __init__(self, obj_handler, player, image, damage, scale=SCALE):
        super().__init__()

        self.obj_handler = obj_handler

        self.image = pygame.image.load(f"assets/sprites/weapons/{image}.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))
        self.base_image = self.image
        self.rect = self.image.get_rect()

        self.player = player
        self.damage = damage

        self.rect.x = self.player.rect.centerx
        self.rect.y = self.player.rect.centery

        self.time = 0
        self.weapon_swing = WeaponSwing(self)
        self.starting_position = [self.rect.bottomleft[0] - 1, self.rect.bottomleft[1]]

    def enemy_collision(self):
        for enemy in self.obj_handler.enemy_group:
            if (
                    pygame.sprite.collide_mask(self.player.weapon, enemy)
                    and enemy.is_dead is False
            ):
                #self.player.weapon.special_effect(enemy)
                enemy.life -= self.player.weapon.damage #* self.game.player.strength
                #enemy.entity_animation.hurt_timer = pygame.time.get_ticks()
                #self.game.sound_manager.play_hit_sound()
                #enemy.weapon_hurt_cooldown = pygame.time.get_ticks()
                enemy.check_death()

    def update(self):
        if self.weapon_swing.counter == 10:
            self.original_image = pygame.transform.flip(self.base_image, 1, 0)
            self.player.attacking = False
            self.weapon_swing.counter = 0
        if self.player.attacking and self.weapon_swing.counter <= 10:
            self.weapon_swing.swing()
            self.enemy_collision()
        else:
            self.weapon_swing.rotate()



