import pygame, csv
from os import listdir

from pygame.sprite import AbstractGroup

from .constants import *
from .utils import *


class Map:
    def __init__(self, obj_handler, level) -> None:
        self.obj_handler = obj_handler
        self.files_path = f"assets/levels/{level}"

        self.create_map()


    def create_map(self):
        tiles = self.load_tiles()

        for file, tileset in tiles.items():
            for y, row in enumerate(tileset):
                for x, tile in enumerate(row):
                    if int(tile) > 0:
                        tile = Tile(f"{file}/{tile.strip()}.png", x * 16 * SCALE, y * 16 * SCALE, scale=SCALE)

                        if file == "wall":
                            self.obj_handler.wall_sprites.add(tile)
                        
                        if file == "floor":
                            self.obj_handler.floor_sprites.add(tile)

                        if file == "objects":
                            self.obj_handler.objects_sprites.add(tile)


    def load_tiles(self):
        files = {}
        for file in listdir(self.files_path):
            world_data = []
            column_data = []
            with open(f"{self.files_path}/{file}", newline="") as csvfile:
                reader = csv.reader(csvfile, delimiter=",")
                for x, row in enumerate(reader):
                    column_data = []
                    for y, tile in enumerate(row):
                        column_data.append(tile)
                    world_data.append(column_data)
            files[file[:-4]] = world_data
        return files



class Tile(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y, scale=SCALE) -> None:
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(f"assets/tilesets/{image_path}")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale, self.image.get_height() * scale))

        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y