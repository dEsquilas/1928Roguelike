import arcade
from helpers.Consts import *

class PickupBase(arcade.Sprite):
    def __init__(self, texture, position):
        super().__init__()
        self.texture = arcade.load_texture(texture)
        self.scale = TILE_SCALING
        self.center_x = position[0]
        self.center_y = position[1]
        self.sound = None
        self.should_remove = False

    def apply_effect(self, player):
        pass