import pygame
from os import listdir

class Animation:
    def __init__(self, spritesheet_path: list, delay, repeat=True):
        self.spritesheet_path = spritesheet_path
        self.delay = delay
        self.repeat = repeat

        self.animation = self.create_animation()

    def create_animation(self):
        animation_list = []
        num_of_frames = len(listdir(self.spritesheet_path))

        for i in range(1, num_of_frames):
            image = pygame.image.load(f"{self.spritesheet_path}\\sprite-{i}.png").convert_alpha()
            animation_list.append(image)

        return animation_list
