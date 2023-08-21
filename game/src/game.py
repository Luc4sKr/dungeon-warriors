import pygame, sys

from .constants import *
from .utils import *

from .menu import MainMenu
from .objectHandler import ObjectHandler
from .map import Map


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(RESOLUTION)
        pygame.display.set_caption("Dungeon Warriors")
        
        self.clock = pygame.time.Clock()
        self.main_menu = MainMenu(self)
        self.game_over = False

    def start(self):
        #self.main_menu.run()
        self.new_game()

    def new_game(self, map=1):
        self.game_over = False
        self.object_handler = ObjectHandler()
        self.map = Map(self.object_handler, map)

        self.run()

    def run(self):        
        while not self.game_over:
            self.clock.tick(FPS)
            self.check_events()
            self.draw()
            self.update()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
                pygame.quit()
                sys.exit()

    def update(self):
        self.object_handler.update()
        pygame.display.flip()

    def draw(self):
        self.screen.fill(BLACK)
        self.object_handler.draw(self.screen)

        draw_text(self.screen, f"FPS: {self.clock.get_fps():.2f}", 16, WHITE, 10, 50, topleft=True)

        