import pygame

class Image:
    def __init__(self, image_path, width=16, height=16) -> None:
        self.__image = pygame.image.load(image_path).convert_alpha()
        self.__width = width
        self.__height = height

    @property
    def image(self):
        return self.__image
    
    @property
    def width(self):
        return self.__width
    
    @property
    def height(self):
        return self.__height