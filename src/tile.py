import pygame

from .image import Image
from .object import Object

class Tile(Object):
    def __init__(self, obj_handler, image: Image, pos_x, pos_y):
        super().__init__(obj_handler, pos_x, pos_y)
        self.tile_img = image

        self.image = image.image
        self.rect = self.image.get_rect()
        
        self.rect.x = pos_x
        self.rect.y = pos_y