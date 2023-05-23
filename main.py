import pygame
import sys

from src.config import *
from src.player import Player
from src.image import Image
from src.spritesheet import Spritesheet
from src.animation import Animation

from src.object_handler import ObjectHandler

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption("Dungeon Warriors")

        self.clock = pygame.time.Clock()
        self.game_over = False
        self.delta_time = 1
        self.global_event = pygame.USEREVENT
        pygame.time.set_timer(self.global_event, 40)

        self.new_game()

    def new_game(self):
        self.object_handler = ObjectHandler(self)

    def update(self):
        self.object_handler.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(BLACK)
        self.object_handler.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
                pygame.quit()
                sys.exit()

    def run(self):
        while not self.game_over:
            self.clock.tick(FPS)
            
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
