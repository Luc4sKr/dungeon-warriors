import pygame

from .utils import *
from .constants import *

from .entity import AnimatedEntity
from .weapon import Weapon

from .menu import GameOverMenu


class Player(AnimatedEntity):
    def __init__(self, obj_handler, animation, model, character, image, pos: tuple, scale=SCALE) -> None:
        super().__init__(obj_handler, animation, image, pos, speed=character.speed, life=character.life, scale=scale)

        self.obj_handler = obj_handler
        self.model = model
        self.character = character

        self.weapon = Weapon(self.obj_handler, self, self.character.weapon.name.lower(), self.character.weapon.damage)
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

    def enemy_collide(self):
        for enemy in self.obj_handler.enemy_group:
            if pygame.sprite.collide_mask(self, enemy) and not self.is_invisible:
                self.life -= enemy.damage
                self.is_invisible = True

    def invisible_manager(self):
        if pygame.time.get_ticks() - self.invisible_time > self.invisible_cooldown and self.is_invisible:
            self.invisible_time = pygame.time.get_ticks()
            self.is_invisible = False

    def check_death(self):
        if self.life <= 0:
            self.model.save_data()
            self.is_dead = True
            self.obj_handler.game.game_over = True
            self.game_over_menu = GameOverMenu(self.obj_handler.game)
            self.game_over_menu.run()

    def draw_username(self, screen):
        self.name_text = return_text(self.model.username, 12, WHITE, self.rect.centerx, self.rect.top)
        screen.blit(self.name_text[0], (self.name_text[1].topleft + self.obj_handler.camera.offset))

    def update(self):
        self.input()
        self.animation_control()
        self.enemy_collide()
        self.check_death()
        self.invisible_manager()

