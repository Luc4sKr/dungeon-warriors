import pygame

from ..utils import *
from .. constants import *


class Slider:
    def __init__(self, left, top, width, height, color, max_value) -> None:
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.color = color
        self.max_value = max_value
        self.value = max_value

        self.slider_border = pygame.Rect(int(self.left - 3), int(self.top - 3), int(self.width + 6), int(self.height + 6))
        self.slider = pygame.Rect(int(self.left), int(self.top), int(self.value), int(self.height))

    def draw(self, screen):
        pygame.draw.rect(screen, BLACK, self.slider_border)
        pygame.draw.rect(screen, self.color, self.slider)

    def update(self, value):
        self.slider = pygame.Rect(int(self.left), int(self.top), int((value * self.width) / self.max_value), int(self.height))

