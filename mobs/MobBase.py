import arcade
import math
from helpers.Consts import *
from helpers.Attributes import Attributes
from helpers.Sounds import ssounds

class MobBase(arcade.Sprite):
    def __init__(self, position, attr=Attributes(100, 5, 0.1, 10), id=0):
        super().__init__()
        self.texture = arcade.load_texture("./assets/sprites/slime.png")
        self.scale = TILE_SCALING
        self.center_x = position[0] * TILE_SCALING
        self.center_y = position[1] * TILE_SCALING

        self.id = id

        self.speed_x = 0
        self.speed_y = 0

        self.should_remove = False

        # Main Attr

        self.attr = attr

    def update_movement(self, player):
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
        to_move_x = - normalized_direction_x * self.attr.get("speed")
        to_move_y = - normalized_direction_y * self.attr.get("speed")

        self.center_x += to_move_x
        self.center_y += to_move_y

    def check_mob_damage_collisions(self, bullets):
        for bullet in bullets:
            if arcade.check_for_collision(self, bullet):
                self.attr.set("health", self.attr.get("health") - bullet.attack_dmg)
                if self.attr.get("health") <= 0:
                    self.should_remove = True
                    ssounds.play("mob_dead")

    def custom_update(self, player):
        self.check_mob_damage_collisions(player.bullets)
        self.update_movement(player.sprite)