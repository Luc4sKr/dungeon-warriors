import pygame
import sys

from src.config import *
from src.menu import MainMenu
from src.level import Level


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption("Dungeon Warriors")
        self.clock = pygame.time.Clock()

        self.game_over = False

        self.main_menu = MainMenu(self)

    def new_game(self):
        self.game_over = False
        self.level = Level(self, "level-1")

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
                pygame.quit()
                sys.exit()

    def update(self):
        self.level.update()
        pygame.display.flip()

        pygame.display.set_caption(f"FPS: {self.clock.get_fps()}")

    def draw(self):
        self.screen.fill(BLACK)
        self.level.draw()

    def run(self):
        self.new_game()
        
        while not self.game_over:
            self.clock.tick(FPS)

            self.check_events()
            self.draw()
            self.update()

if __name__ == "__main__":
    game = Game()
