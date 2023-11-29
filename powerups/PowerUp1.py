import arcade
from helpers.Consts import *


class PowerUp1(arcade.Sprite):
    def __init__(self, position):
        super().__init__()
        self.texture = arcade.load_texture("./assets/sprites/powerup1.png")
        self.center_x = position[0] * TILE_SCALING
        self.center_y = position[1] * TILE_SCALING
        self.scale = TILE_SCALING

        self.oscilate_value = 10
        self.direction = 1
        self.origin_y = position[1] * TILE_SCALING


        self.attr_modifier_id = "fire_speed"
        self.attr_modifier_type = 2
        self.attr_modifier_value = 0.25


    def apply_effect(self, player):
        if self.attr_modifier_type == 1:
            player.attr[self.attr_modifier_id] += self.attr_modifier_value
        elif self.attr_modifier_type == 2:
            player.attr[self.attr_modifier_id] *= self.attr_modifier_value

    def update(self):

        movement = 0.5

        if self.direction == 1:
            if abs(self.center_y - self.origin_y) < self.oscilate_value:
                self.center_y += movement
            else:
                self.direction = -1
                self.center_y -= movement
        if self.direction == -1:
            if abs(self.center_y - self.origin_y) < self.oscilate_value:
                self.center_y -= movement
            else:
                self.direction = 1
                self.center_y += movement