import pygame

class Image:
    def __init__(self, image_path, scale=1, rotation=0) -> None:
        self.__scale = scale
        self.__rotation =  rotation

        self.__image = pygame.image.load(image_path).convert_alpha()
        self.__image = pygame.transform.scale(self.__image, (self.__image.get_width() * scale, self.__image.get_height() * scale))

    def move_to(self, dx, dy):
        self.__pos_x = dx
        self.__pos_y = dy

    def translate(self, dx, dy):
        self.__pos_x += dx
        self.__pos_y += dy

    def scale(self, factor):
        self.__scale *= factor

    def scaleTo(self, value):
        self.__scale = value
        

    @property
    def image(self):
        return self.__image
    
    

