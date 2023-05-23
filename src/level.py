import csv

from .config import *
from .tile import Tile

class Level:
    def __init__(self, game, csv_file) -> None:
        self.game = game
        self.csv_file = csv_file

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

    def process_data(self):
        data = self.open_file()

        for y, row in enumerate(data):
            for x, tile in enumerate(row):
                if int(tile) == 1:
                    img = self.game.object_handler.TILE_FLOOR_1
                    new_tile = Tile(self.game.object_handler.TILE_FLOOR_1, x * img.image.get_width(), y * img.image.get_height())
                    self.game.object_handler.add_sprite(new_tile)