import arcade
from helpers.Consts import *

class PlayerSprite(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.texture = arcade.load_texture("./assets/sprites/player.png")
        self.scale = TILE_SCALING
        self.center_x = 100
        self.center_y = 100

        self.is_attacking = False
        self.last_attack_time = 0
        self.last_damage_time = 0

        self.direction = UP

        self.speed_x = 0
        self.speed_y = 0

    def update(self, is_moving, speed):

        self.speed_x = 0
        self.speed_y = 0

        self.speed_x += speed if is_moving[RIGHT] else 0
        self.speed_x += -speed if is_moving[LEFT] else 0
        self.speed_y += speed if is_moving[UP] else 0
        self.speed_y += -speed if is_moving[DOWN] else 0

        self.center_x += self.speed_x
        self.center_y += self.speed_y
