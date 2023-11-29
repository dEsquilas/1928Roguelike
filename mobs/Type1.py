import arcade
import math
from helpers.Consts import *

class Type1(arcade.Sprite):
    def __init__(self, position):
        super().__init__()
        self.texture = arcade.load_texture("./assets/sprites/slime.png")
        self.scale = TILE_SCALING
        self.center_x = position[0] * TILE_SCALING
        self.center_y = position[1] * TILE_SCALING

        self.is_moving_up = False
        self.is_moving_down = False
        self.is_moving_left = False
        self.is_moving_right = False

        self.speed_x = 0
        self.speed_y = 0

        # Main Attr

        self.health = 100
        self.speed = 1
        self.attack_dmg = 10

    def update(self, player):

        # update sprite for player direction

        direction_x = self.center_x - player.center_x
        direction_y = self.center_y - player.center_y

        magnitude = math.sqrt(direction_x ** 2 + direction_y ** 2)

        # Normalizar las direcciones dividiendo por la magnitud
        if magnitude > 0:
            normalized_direction_x = direction_x / magnitude
            normalized_direction_y = direction_y / magnitude
        else:
            # En caso de que las direcciones tengan magnitud cero (evita divisiones por cero)
            normalized_direction_x = 0
            normalized_direction_y = 0

        # Calcular la cantidad de movimiento en cada dirección
        to_move_x = - normalized_direction_x * self.speed
        to_move_y = - normalized_direction_y * self.speed

        self.center_x += to_move_x
        self.center_y += to_move_y




