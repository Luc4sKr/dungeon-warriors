import pygame
import sys

from src.config import *
from src.player import Player
from src.image import Image

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode(RESOLUTION)
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.delta_time = 1
        self.global_event = pygame.USEREVENT
        pygame.time.set_timer(self.global_event, 40)

        self.new_game()

    def new_game(self):
        self.all_sprites = pygame.sprite.Group()

        player_img = Image("assets\sprites\warrior\knight_f_hit_anim_f0.png")
        self.player = Player(player_img, 100, 100, 100)

        self.all_sprites.add(self.player)

    def update(self):
        self.all_sprites.update()
        pygame.display.flip()

    def draw(self):
        # colocar o object_render aqui dps
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
                pygame.quit()
                sys.exit()

    def run(self):
        while not self.game_over:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
