import arcade
from helpers.Consts import *


class PowerUp1(arcade.Sprite):
    def __init__(self, position):
        super().__init__()
        self.texture = arcade.load_texture("./assets/sprites/powerup1.png")
        self.center_x = position[0] * TILE_SCALING
        self.center_y = position[1] * TILE_SCALING
        self.scale = TILE_SCALING


    def update(self):
        pass