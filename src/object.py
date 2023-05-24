import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, object_handler, pos_x, pos_y):
        super().__init__(object_handler.sprite_list)

        self.__pos_x = pos_x
        self.__pos_y = pos_y

    @property
    def pos_x(self):
        return self.__pos_x
    
    @property
    def pos_y(self):
        return self.__pos_y
    

