import pygame

class Object(pygame.sprite.Sprite):
    def __init__(self, object_handler, image, pos_x, pos_y):
        super().__init__(object_handler.sprite_list)

        self.image = image.image
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.rect = self.image.get_rect()

    

class Animated_object(Object):
    pass