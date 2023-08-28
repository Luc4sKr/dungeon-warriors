import pygame
import requests
import pickle
import os

from .constants import *

from .ui.slider import Slider

from .models.player_model import PlayerModel
from .models.character_model import CharacterModel

from .spritesheet import Spritesheet
from .animation import Animation
from .player import Player
from .camera import Camera
from .enemy_spawn import EnemySpawn

class ObjectHandler:
    def __init__(self, game) -> None:
        self.game = game

        self.load_groups()
        self.load_player()
        self.load_enemy()
        self.load_camera()

        self.enemy_spawn = EnemySpawn(self)

    def load_groups(self):
        self.wall_sprites = pygame.sprite.Group()
        self.floor_sprites = pygame.sprite.Group()
        self.objects_sprites = pygame.sprite.Group()

        self.player_group = pygame.sprite.GroupSingle()
        self.enemy_group = pygame.sprite.Group()
        self.weapon_group = pygame.sprite.GroupSingle()

    def load_player(self):
        player_idle_spritesheet = Spritesheet("assets/sprites/characters/warrior/idle", 240, SCALE)
        player_run_spritesheet = Spritesheet("assets/sprites/characters/warrior/run", 100, SCALE)
        
        player_anim = Animation()
        player_anim.add(PLAYER_IDLE, player_idle_spritesheet)
        player_anim.add(PLAYER_RUN, player_run_spritesheet)

        player_request = requests.get("http://127.0.0.1:5000/player/1")
        player_model = PlayerModel(**player_request.json()["data"])

        character_request = requests.get("http://127.0.0.1:5000/character/1")
        character_mdoel = CharacterModel(**character_request.json()["data"])

        """
        print(f"{os.getcwd()}/bin/")
        with open(os.path.join(os.getcwd() + "/bin", "player_model.pkl"), "wb") as file:
            pickle.dump(player_model, file)
            print("foi")
        """
        
        self.player = Player(self, player_anim, player_model, character_mdoel, "assets/sprites/characters/warrior/sprite.png", (0, 0), scale=SCALE)
        self.player_group.add(self.player)
        self.player_life_slider = Slider(10, 10, 200, 20, PURPLE, self.player.life)

    def load_enemy(self):
        enemy_idle_spritesheet = Spritesheet("assets/sprites/enemies/demon/idle", 240, SCALE)

        self.enemy_anim = Animation()
        self.enemy_anim.add(ENEMY_IDLE, enemy_idle_spritesheet)

    def load_camera(self):
        self.camera = Camera(self.player, WIDTH, HEIGHT)

    def update(self):
        self.player_group.update()
        self.weapon_group.update()
        self.enemy_group.update()
        self.camera.scroll()

        self.enemy_spawn.check_enemies()
        self.player_life_slider.update(self.player.life)

    def draw(self, screen):
        for sprite in self.wall_sprites:
            screen.blit(sprite.image, (sprite.rect.topleft + self.camera.offset)) 

        for sprite in self.floor_sprites:
            screen.blit(sprite.image, (sprite.rect.topleft + self.camera.offset))

        for sprite in self.objects_sprites:
            screen.blit(sprite.image, (sprite.rect.topleft + self.camera.offset))

        for sprite in self.enemy_group:
            screen.blit(sprite.image, (sprite.rect.topleft + self.camera.offset))
        
        for sprite in self.player_group:
            screen.blit(sprite.image, (sprite.rect.topleft + self.camera.offset))

        for sprite in self.weapon_group:
            screen.blit(sprite.image, (sprite.rect.topleft + self.camera.offset))


        #self.player.draw_username(screen)
        self.player_life_slider.draw(screen)
        