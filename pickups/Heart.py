import arcade
from helpers.Consts import *
from pickups.PickupBase import PickupBase

class Heart(PickupBase):
    def __init__(self, position):
        super().__init__("./assets/sprites/heart.png", position)
        self.sound = "glup"
        self.scale = 1

    def apply_effect(self, player):
        player.current_hp += 10