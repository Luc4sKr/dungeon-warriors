import pygame

from .image import Image
from .object import Object

class Tile(Object):
    def __init__(self, obj_handler, image: Image, pos_x, pos_y):
        super().__init__(obj_handler, image, pos_x, pos_y)
        
        self.rect.x = pos_x
        self.rect.y = pos_y