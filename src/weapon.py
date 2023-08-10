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
        dx = mx - self.weapon.player.rect.centerx - self.weapon.player.game.camera.offset.x
        dy = my - self.weapon.player.rect.centery - self.weapon.player.game.camera.offset.y

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
        self.weapon.hitbox = pygame.mask.from_surface(self.weapon.image)
        self.offset_rotated = pygame.math.Vector2(0, -35).rotate(-self.angle)

    def swing(self):
        self.angle += 20 * self.swing_side
        position = self.weapon.player.hitbox.center
        self.weapon.image = pygame.transform.rotozoom(self.weapon.original_image, self.angle, 1)
        offset_rotated = self.offset.rotate(-self.angle)
        self.weapon.rect = self.weapon.image.get_rect(center=position + offset_rotated)
        # self.rect_mask = get_mask_rect(self.image, *self.rect.topleft)
        self.weapon.hitbox = pygame.mask.from_surface(self.weapon.image)
        self.counter += 1


class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, image, damage, scale=SCALE):
        super().__init__()

        self.image = pygame.image.load(f"assets/sprites/weapons/{image}.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))
        self.base_image = self.image
        self.rect = self.image.get_rect()
        self.hitbox = get_mask_rect(self.base_image, *self.rect.topleft)

        self.player = player

        self.damage = damage

        self.rect.x = self.player.rect.centerx
        self.rect.y = self.player.rect.centery

        self.time = 0
        self.weapon_swing = WeaponSwing(self)
        self.starting_position = [self.hitbox.bottomleft[0] - 1, self.hitbox.bottomleft[1]]

    def detect_collision(self):
        if self.game.player.hitbox.colliderect(self.rect):
            self.image = self.image_picked
            self.interaction = True
        else:
            self.image = self.original_image
            self.interaction = False
            self.show_name.reset_line_length()

    def interact(self):
        self.weapon_swing.reset()
        self.player = self.game.player
        self.player.items.append(self)
        if not self.player.weapon:
            self.player.weapon = self
        if self.room == self.game.world_manager.current_room:
            self.room.objects.remove(self)
        self.interaction = False
        self.show_name.reset_line_length()
        self.game.sound_manager.play_get_item_sound()

    def drop(self):
        self.game.sound_manager.play_drop_sound()
        self.room = self.game.world_manager.current_room
        self.player.items.remove(self)
        self.player.weapon = None
        self.game.world_manager.current_room.objects.append(self)
        if self.player.items:
            self.player.weapon = self.player.items[-1]
        self.load_image()
        self.rect = self.image.get_rect()
        self.hitbox = get_mask_rect(self.image, *self.rect.topleft)
        self.rect.x = self.player.rect.x
        self.rect.y = self.player.rect.y
        self.player = None
        self.weapon_swing.offset_rotated = pygame.math.Vector2(0, -25)

    def enemy_collision(self):
        for enemy in self.game.enemy_manager.enemy_list:
            if (
                    pygame.sprite.collide_mask(self.game.player.weapon, enemy)
                    and enemy.dead is False
                    and enemy.can_get_hurt_from_weapon()
            ):
                self.game.player.weapon.special_effect(enemy)
                enemy.hurt = True
                enemy.hp -= self.game.player.weapon.damage * self.game.player.strength
                enemy.entity_animation.hurt_timer = pygame.time.get_ticks()
                self.game.sound_manager.play_hit_sound()
                enemy.weapon_hurt_cooldown = pygame.time.get_ticks()

    def player_update(self):
        self.interaction = False
        if self.weapon_swing.counter == 10:
            self.original_image = pygame.transform.flip(self.original_image, 1, 0)
            self.player.attacking = False
            self.weapon_swing.counter = 0
        if self.player.attacking and self.weapon_swing.counter <= 10:
            self.weapon_swing.swing()
            self.enemy_collision()
        else:
            self.weapon_swing.rotate()

    def draw_shadow(self, surface):
        if self.dropped:
            self.shadow.set_shadow_position()
            self.shadow.draw_shadow(surface)
        else:
            if not self.shadow.shadow_set:
                self.shadow.set_shadow_position()
            if self.player:
                self.shadow.shadow_set = False
            if self.player is None:
                self.shadow.draw_shadow(surface)

    def update(self):
        self.weapon_swing.rotate()

    def draw(self):
        surface = self.room.tile_map.map_surface
        if self.player:
            surface = self.game.screen
        surface.blit(self.image, self.rect)
        if self.interaction:
            self.show_name.draw(surface, self.rect)
        self.show_price.draw(surface)
        self.draw_shadow(surface)






'''
class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, image, damage, scale=SCALE):
        super().__init__()
        self.player = player

        self.image = pygame.image.load(f"assets/sprites/weapons/{image}.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))
        self.base_image = self.image
        self.rect = self.image.get_rect()

        self.rect.center = self.player.rect.center

    def rotate(self):
        mx, my = pygame.mouse.get_pos()
        dx = mx - self.player.rect.centerx
        dy = my - self.player.rect.centery

        self.angle = (180 / math.pi) * math.atan2(dy, dx)

        position = self.player.rect.center
        offset_rotated = self.offset.rotate(-self.angle)
        self.rect = self.image.get_rect(center=position + offset_rotated)
        self.offset_rotated = pygame.math.Vector2(0, -35).rotate(-self.angle)

        self.image = pygame.transform.rotate(self.base_image, self.angle)

    def update(self):
        self.rect.center = self.player.rect.center
'''