import pygame


class Object(pygame.sprite.Sprite):
    def __init__(self, image_path, pos: tuple, scale=1) -> None:
        super().__init__()

        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))

        self.rect = self.image.get_rect()
        self.rect.center = pos


class AnimatedObject(Object):
    def __init__(self, animation, image_path, pos: tuple, scale=1) -> None:
        super().__init__(image_path, pos, scale)

        self.animation = animation
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
