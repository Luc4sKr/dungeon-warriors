import pygame, sys
from abc import ABC

from .config import * 
from .utils import *

class Menu(ABC):
    def __init__(self, game) -> None:
        self.game = game

        self.show = True
        self.mouse_click = False

        self.run()

    def run(self):
        while self.show:
            self.game.clock.tick(FPS)

            self.check_events()
            self.draw()
            self.update()

    def draw(self):
        self.game.screen.fill(BLACK)

    def update(self):
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.show = False
                self.game.game_over = True
                pygame.quit()
                sys.exit()
            self.menu_events(event)


class MainMenu(Menu):
    def __init__(self, game) -> None:
        super().__init__(game)

    def draw(self):
        super().draw()

        draw_text(self.game.screen, "Dungeon Warriors", TITLE_FONT, WHITE, HALF_WIDTH, 50)
        draw_text(self.game.screen, "Press SPACE to play", 16, WHITE, HALF_WIDTH, 440)

    def update(self):
        super().update()

    def menu_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.show = False
                self.game.run()