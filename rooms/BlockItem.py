import arcade
from helpers.Consts import *

class BlockItem(arcade.Sprite):
    def __init__(self, position):
        super().__init__()

        self.texture = arcade.load_texture("./assets/sprites/block_item.png")
        self.center_x = TILE_SCALING * position[0]
        self.center_y = TILE_SCALING * position[1]
        # self.scale = TILE_SCALING #