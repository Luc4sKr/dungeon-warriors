import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, health):
        pygame.sprite.Sprite.__init__(self)

        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__health = health

    @property
    def pos_x(self):
        return self.__pos_x
    
    @property
    def pos_y(self):
        return self.__pos_y
    
    @property
    def health(self):
        return self.__health
    
    @health.setter
    def health(self, value):
        if value <= 0:
            value = 1
        self.health = value

