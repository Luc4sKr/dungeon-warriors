import pygame

from ..utils import *
from ..constants import *


class Button:
    def __init__(self, text, left, top, width, height, callback_function=None, font_size=20, button_color=BLACK, font_color=WHITE, border_color=WHITE, hover_border_color=YELLOW):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.button_color = button_color
        self.base_font_color = font_color
        self.font_color = font_color
        self.base_border_color = border_color
        self.border_color = border_color
        self.hover_border_color = hover_border_color

        self.button_border = pygame.Rect(int(self.left - 2), int(self.top - 2), int(self.width + 4), int(self.height + 4))
        self.button = pygame.Rect(int(self.left), int(self.top), int(self.width), int(self.height))

        self.callback_function = callback_function

    def draw(self, screen):
        pygame.draw.rect(screen, self.border_color, self.button_border)
        pygame.draw.rect(screen, self.button_color, self.button)

        draw_text(screen, self.text, self.font_size, self.font_color, self.left + (self.width / 2), self.top + (self.height / 2))

    def update(self, click):
        self.mouse_pos = pygame.mouse.get_pos()

        self.check_hover()
        self.check_click(click)

    def check_click(self, click):
        if self.check_hover() and click:
            if self.callback_function:
                self.callback_function()

    def check_hover(self):
        if self.button.collidepoint(self.mouse_pos):
            self.border_color = self.hover_border_color
            self.font_color = self.hover_border_color
            return True
        
        self.border_color = self.base_border_color
        self.font_color = self.base_font_color
        return False
    