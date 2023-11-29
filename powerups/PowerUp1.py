import arcade
from helpers.Consts import *


class PowerUp1(arcade.Sprite):
    def __init__(self, position):
        super().__init__()
        self.texture = arcade.load_texture("./assets/sprites/powerup1.png")
        self.center_x = position[0] * TILE_SCALING
        self.center_y = position[1] * TILE_SCALING
        self.scale = TILE_SCALING


        self.attr_modifier_id = "fire_speed"
        self.attr_modifier_type = 2
        self.attr_modifier_value = 0.25


    def apply_effect(self, player):
        if self.attr_modifier_type == 1:
            player.attr[self.attr_modifier_id] += self.attr_modifier_value
        elif self.attr_modifier_type == 2:
            player.attr[self.attr_modifier_id] *= self.attr_modifier_value

    def update(self):
        pass