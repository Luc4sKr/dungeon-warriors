import pygame, sys
from abc import ABC

from .ui.button import Button

from .constants import * 
from .utils import *


class Menu(ABC):
    def __init__(self, game) -> None:
        self.game = game
        self.show_menu = True

    def run(self):
        while self.show_menu:
            self.game.clock.tick(FPS)

            self.check_events()
            self.draw()
            self.update()

    def update(self):
        self.click = False
        pygame.display.flip()

    def draw(self):
        self.game.screen.fill(BLACK)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.show_menu = False
                self.game.game_over = True
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True

            self.menu_events(event)


class MainMenu(Menu):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.click = False

        # menus dependentes
        self.select_map_menu = SelectMapMenu(self.game)

        self.play_btn = Button("PLAY", HALF_WIDTH - 100, PLAY_BTN_TOP, 200, 50, callback_function=self.play)
        self.options_btn = Button("OPTIONS", HALF_WIDTH - 100, OPTIONS_BTN_TOP, 200, 50)
        self.exit_btn = Button("EXIT", HALF_WIDTH - 100, EXIT_BTN_TOP, 200, 50, callback_function=self.exit)

    def update(self):
        self.play_btn.update(self.click)
        self.options_btn.update(self.click)
        self.exit_btn.update(self.click)

        super().update()

    def draw(self):
        super().draw()

        draw_text(self.game.screen, "Dungeon Warriors", TITLE_FONT, WHITE, HALF_WIDTH, 50)

        self.play_btn.draw(self.game.screen)
        self.options_btn.draw(self.game.screen)
        self.exit_btn.draw(self.game.screen)

    def menu_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.show = False
                self.game.new_game()

    def play(self):
        self.show_menu = False
        self.select_map_menu.run()

    def options(self):
        pass

    def exit(self):
        self.show_menu = False
        self.game.game_over = True
        pygame.quit()
        sys.exit()


class SelectMapMenu(Menu):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.click = False

        self.selected_map = None

        self.map_1_btn = Button("MAP 1", HALF_WIDTH - 100, 200, 200, 50, callback_function=self.select_map_1)
        self.map_2_btn = Button("MAP 2", HALF_WIDTH - 100, 260, 200, 50, callback_function=self.select_map_2)

    def menu_events(self, event):
        pass

    def update(self):
        self.map_1_btn.update(self.click)
        self.map_2_btn.update(self.click)

        super().update()

    def draw(self):
        super().draw()

        draw_text(self.game.screen, "Select Map", TITLE_FONT, WHITE, HALF_WIDTH, 50)

        self.map_1_btn.draw(self.game.screen)
        self.map_2_btn.draw(self.game.screen)

    def select_map_1(self):
        self.selected_map = 1
        self.run_game()

    def select_map_2(self):
        self.selected_map = 2
        self.run_game()

    def run_game(self):
        self.show_menu = False
        self.game.new_game(self.selected_map)


class LoginMenu(Menu):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.click = False

    def menu_events(self, event):
        pass

    def update(self):
        super().update()

    def draw(self):
        super().draw()

        draw_text(self.game.screen, "Login", TITLE_FONT, WHITE, HALF_WIDTH, 50)


class GameOverMenu(Menu):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.click = False

        self.back_to_menu_btn = Button("BACK TO MENU", HALF_WIDTH - 100, 300, 200, 50, callback_function=self.back_to_menu)

    def menu_events(self, event):
        pass

    def update(self):
        self.back_to_menu_btn.update(self.click)

        super().update()

    def draw(self):
        super().draw()

        draw_text(self.game.screen, "Game Over", TITLE_FONT, RED, HALF_WIDTH, 50)

        self.back_to_menu_btn.draw(self.game.screen)

    def back_to_menu(self):
        self.show_menu = False
        mainmenu = MainMenu(self.game)
        mainmenu.run()


class PauseMenu(Menu):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.click = False

        self.back_to_game = Button("BACK TO MENU", HALF_WIDTH - 100, 300, 200, 50, callback_function=self.back_to_menu)
        self.back_to_menu_btn = Button("BACK TO MENU", HALF_WIDTH - 100, 300, 200, 50, callback_function=self.back_to_menu)

    def menu_events(self, event):
        pass

    def update(self):
        self.back_to_menu_btn.update(self.click)

        super().update()

    def draw(self):
        super().draw()

        self.back_to_menu_btn.draw(self.game.screen)

        draw_text(self.game.screen, "Pause", TITLE_FONT, WHITE, HALF_WIDTH, 50)

    def back_to_game(self):
        pass

    def back_to_menu(self):
        self.show_menu = False
        mainmenu = MainMenu(self.game)
        mainmenu.run()