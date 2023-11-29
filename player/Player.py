import arcade
from helpers.Consts import *

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

        self.is_attacking = False
        self.last_attack_time = 0
        self.last_damage_time = 0

        self.direction = D_UP

        self.speed_x = 0
        self.speed_y = 0

        # Main Attr

        self.attr = {}
        self.attr['health'] = 100
        self.attr['speed'] = 5
        self.attr['fire_speed'] = 0.5
        self.attr['attack_dmg'] = 10

    def update(self):

        self.speed_x = 0
        self.speed_y = 0

        self.speed_x += self.attr["speed"] if self.is_moving_right else 0
        self.speed_x += -self.attr["speed"] if self.is_moving_left else 0
        self.speed_y += self.attr["speed"] if self.is_moving_up else 0
        self.speed_y += -self.attr["speed"] if self.is_moving_down else 0

        if self.is_moving_up:
            self.direction = D_UP
        elif self.is_moving_down:
            self.direction = D_DOWN
        elif self.is_moving_left:
            self.direction = D_LEFT
        elif self.is_moving_right:
            self.direction = D_RIGHT

        #print(self.speed_x, self.speed_y)

        self.center_x += self.speed_x
        self.center_y += self.speed_y


