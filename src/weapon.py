import pygame
import math

from .config import *
from .object import Object


bow = {
    "unarmed": f"{WEAPONS_PATH}/bow/unarmed.png",
    "active": f"{WEAPONS_PATH}/bow/active.png",
    "arrow": f"{WEAPONS_PATH}/bow/arrow.png"
}

class Bow(Object):
    def __init__(self, image_path, pos: tuple, scale=1) -> None:
        super().__init__(image_path, pos, scale)

        self.base_image = self.image

    def shoot(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # and not self.shot and not self.game.weapon.reloding
                self.image = pygame.image.load(bow["active"])

    def rotation(self):
        self.mouse_cords = pygame.mouse.get_pos()
        self.change_mouse_weapon_x = (self.mouse_cords[0] - self.rect.centerx)
        self.change_mouse_weapon_y = (self.mouse_cords[1] - self.rect.centery)

        self.angle = math.degrees(math.atan2(self.change_mouse_weapon_y, self.change_mouse_weapon_x))
        self.angle = (self.angle) % 360

        self.image = pygame.transform.rotate(self.base_image, -self.angle)

    def update(self):
        self.rotation()


        