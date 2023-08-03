import pygame

from .utils import *


class Entity(pygame.sprite.Sprite):
    def __init__(self, obj_handler, image_path, pos: tuple, speed, scale=1) -> None:
        super().__init__()

        self.obj_handler = obj_handler

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))

        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.speed = speed
        self.dead = False

        self.direction = pygame.math.Vector2(0, 0)

    def wall_collision(self, direction):
        for wall in self.obj_handler.wall_sprites:
            
            if wall.rect.colliderect(self.rect):
                if direction == "horizontal":
                    if self.direction.x > 0: # moving right
                        self.rect.right = wall.rect.left
                    if self.direction.x < 0: # moving left
                        self.rect.left = wall.rect.right
                
                if direction == "vertical":
                    if self.direction.y > 0: # moving down
                        self.rect.bottom = wall.rect.top
                    if self.direction.y < 0: # moving up
                        self.rect.top = wall.rect.bottom
            

class AnimatedEntity(Entity):
    def __init__(self, game, animation, image_path, pos: tuple, speed, scale=1) -> None:
        super().__init__(game, image_path, pos, speed, scale)

        self.animation = animation
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()