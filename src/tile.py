import pygame

from .image import Image
from .object import Object

class Tile(pygame.sprite.Sprite):
    def __init__(self, image: Image, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)

        self.image = image.image
        self.rect = self.image.get_rect()
        
        self.rect.x = pos_x
        self.rect.y = pos_y