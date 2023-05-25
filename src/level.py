import pygame
import csv

from .camera import YSortCameraGroup
from .tile import Tile

class Level:
    def __init__(self, game, csv_file) -> None:
        self.game = game
        self.csv_file = csv_file

        self.sprites_group = YSortCameraGroup()
        self.floor_sprites = pygame.sprite.Group()
        self.wall_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        data = self.open_file()

        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if int(tile) == 1:
                    img = self.game.object_handler.TILE_FLOOR_1
                    tile = Tile(img, x * 16, y * 16)
                    self.floor_sprites.add(tile)

    def open_file(self):
        world_data = []
        c = []
        with open(self.csv_file, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for x, row in enumerate(reader):
                for y, tile in enumerate(row):
                    c.append(tile)
                world_data.append(c)      
        return world_data
    
    def run(self):
        self.sprites_group.custom_draw(self.game.object_handler.player)
        self.sprites_group.update()
