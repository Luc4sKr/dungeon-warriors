import pygame
import csv

from .config import *
from .object import Object

class Tilemap:
    def __init__(self, level) -> None:

        self.level = level
        
        self.all_sprites = pygame.sprite.Group()
        self.wall_sprites = pygame.sprite.Group()

        self.csv_file = f"assets/levels/{level.level}/map.csv"
        self.floor_sprites = pygame.sprite.Group()
        self.wall_sprites = pygame.sprite.Group()

        self.create_map()

    def create_map(self):
        data = self.open_file()

        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                img_obj = Object(f"assets/tilesets/map/{int(tile)}.png", ( x * 16 * SCALE, y * 16 * SCALE), scale=SCALE)
                self.all_sprites.add(img_obj)

                if int(tile) in WALL_TILES:
                    self.wall_sprites.add(img_obj)

        print(self.wall_sprites)

    def open_file(self):
        world_data = []
        column_data = []
        with open(self.csv_file, newline="") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for x, row in enumerate(reader):
                column_data = []
                for y, tile in enumerate(row):
                    column_data.append(tile)
                world_data.append(column_data)
        return world_data
    
    def draw(self, screen):
        self.floor_sprites.draw(screen)

    def update(self):
        self.floor_sprites.update()