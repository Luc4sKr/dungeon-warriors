import pygame
from .constants import *


def draw_text(screen, text, size, color, x, y, style=PIXEL_FONT, topleft=False):
    fonte = pygame.font.Font(style, size)
    text_obj = fonte.render(text, False, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)

    if topleft:
        text_rect.topleft = (x, y)
        
    screen.blit(text_obj, text_rect)

def return_text(text, size, color, x, y, style=PIXEL_FONT, topleft=False):
    fonte = pygame.font.Font(style, size)
    text_obj = fonte.render(text, False, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)

    if topleft:
        text_rect.topleft = (x, y)
        
    return text_obj, text_rect


def get_mask_rect(surf, top=0, left=0):
    """Returns minimal bounding rectangle of an image"""
    surf_mask = pygame.mask.from_surface(surf)
    rect_list = surf_mask.get_bounding_rects()
    if rect_list:
        surf_mask_rect = rect_list[0].unionall(rect_list)
        surf_mask_rect.move_ip(top, left)
        return surf_mask_rect