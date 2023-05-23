import pygame

from .config import *
from .object import Object
from .image import Image

class Player(Object):
    def __init__(self, image: Image, pos_x, pos_y, health, scale=1, rotation=0) -> None:
        super().__init__(pos_x, pos_y, health, scale, rotation)
    
        self.image = image.image
        self.rect = self.image.get_rect()
        self.rect.center = (HALF_WIDTH, HALF_HEIGHT)

    def update(self):
        pass
