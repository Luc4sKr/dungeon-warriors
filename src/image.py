import pygame
from abc import ABC

class Image(ABC):
    def __init__(self, image_path, scale=1, rotation=0) -> None:
        self.__scale = scale
        self.__rotation =  rotation

        self.__image = pygame.image.load(image_path).convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (self.__image.get_width() * scale, self.__image.get_height() * scale))

    def scaleTo(self, factor):
        self.__image = pygame.transform.scale(self.__image, (self.__image.get_width() * factor, self.__image.get_height() * factor))

    @property
    def image(self):
        return self.__image
    
    

