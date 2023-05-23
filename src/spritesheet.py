from os import listdir

from .image import Image

class Spritesheet:
    def __init__(self, path, delay, scale=1, rotation=0):
        self.path = path
        self.delay = delay
        self.scale = scale
        self.rotation = rotation

        self.sprite_list = self.create_spritesheet()

    def create_spritesheet(self):
        image_list = []
        num_of_frames = len(listdir(self.path))

        for i in range(1, num_of_frames):
            image = Image(f"{self.path}\\sprite-{i}.png", scale=self.scale, rotation=self.rotation)
            image_list.append(image)
        return image_list