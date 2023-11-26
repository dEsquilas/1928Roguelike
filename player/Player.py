import arcade
from helpers.consts import *

class Player(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture("./assets/sprites/player.png")
        self.scale = TILE_SCALING
        self.center_x = 100
        self.center_y = 100

        self.is_moving_up = False
        self.is_moving_down = False
        self.is_moving_left = False
        self.is_moving_right = False

        self.speed_x = 0
        self.speed_y = 0

        # Main Attr

        self.health = 100
        self.speed = 5

    def update(self):

        self.speed_x = 0
        self.speed_y = 0

        self.speed_x += self.speed if self.is_moving_right else 0
        self.speed_x += -self.speed if self.is_moving_left else 0
        self.speed_y += self.speed if self.is_moving_up else 0
        self.speed_y += -self.speed if self.is_moving_down else 0

        #print(self.speed_x, self.speed_y)

        self.center_x += self.speed_x
        self.center_y += self.speed_y


