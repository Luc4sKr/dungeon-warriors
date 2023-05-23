import pygame
import sys

from src.config import *
from src.player import Player
from src.image import Image
from src.spritesheet import Spritesheet
from src.animation import Animation

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

        player_img = Image("assets\sprites\warrior\idle\sprite-1.png", 3)
        player_idle_spritesheet = Spritesheet("assets\sprites\warrior\idle", 240, 3)
        player_run_spritesheet = Spritesheet("assets\sprites\warrior\\run", 100, 3)

        player_anim = Animation()
        player_anim.add(1, player_idle_spritesheet)
        player_anim.add(2, player_run_spritesheet)

        self.player = Player(player_img, player_anim, 100, 100, 100)

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
            self.clock.tick(FPS)
            
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    game = Game()
    game.run()
