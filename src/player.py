import pygame
from math import sqrt, sin, cos

from .config import *
from .object import Object
from .image import Image
from .animation import Animation
from .spritesheet import Spritesheet

class Player(Object):
    def __init__(self, obj_handler, image: Image, animation: Animation, pos_x, pos_y) -> None:
        super().__init__(obj_handler, image, pos_x, pos_y)
    
        self.animation = animation
        self.direction = pygame.math.Vector2()

        self.speed = 5
        self.is_running = False
        self.invert_sprite = False

        self.rect.center = (pos_x, pos_y)

        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()

        self.animation.select(PLAYER_IDLE)

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

    def move(self):
        self.is_running = False
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            self.is_running = True
        
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

    def animation_control(self):
        self.animation.select(PLAYER_IDLE)
        if self.is_running:
            self.animation.select(PLAYER_RUN)

        self.image = self.animation.update_animation()
        self.image = pygame.transform.flip(self.image, self.invert_sprite, False)

    def draw(self):
        pass

    def update(self):
        self.input()
        self.move()
        self.animation_control()
