import copy
import arcade
from mobs.MobBase import MobBase
from powerups.PowerUpBase import PowerUpBase
from helpers.Attributes import Attributes
from helpers.Consts import *

class Room():
    def __init__(self, tile_file):
        super().__init__()

        self.tile_map = arcade.load_tilemap(tile_file, TILE_SCALING, {})
        self.floor = arcade.Scene.from_tilemap(self.tile_map)
        self.mobs = []
        self.pickups = arcade.SpriteList()
        self.powerups = arcade.SpriteList()
        self.walls = self.get_walls()
        self.obstacles = arcade.SpriteList()

        # add elements

        attr = Attributes(100, 0.5, 0.1, 10)

        mobs1 = MobBase((250, 100), copy.deepcopy(attr), 1)
        mobs2 = MobBase((300, 150), copy.deepcopy(attr), 2)

        self.mobs.append(mobs1)
        self.mobs.append(mobs2)

        powerup = PowerUpBase((450, 200))

        self.powerups.append(powerup)

    def get_walls(self):
        walls = arcade.SpriteList()
        for sprite in self.floor.get_sprite_list("Walls"):
            walls.append(sprite)
        return walls

    def mobs_update(self, player):
        for mob in self.mobs:
            mob.custom_update(player)
            if mob.should_remove:
                self.mobs.remove(mob)

    def mobs_draw(self):
        for mob in self.mobs:
            mob.draw()

    def powerups_update(self):
        for powerup in self.powerups:
            if powerup.should_remove:
                self.powerups.remove(powerup)

    def update(self, player):
        self.floor.update()
        self.mobs_update(player)
        self.pickups.update()
        self.powerups_update()
        self.walls.update()
        self.obstacles.update()

    def draw(self):
        self.floor.draw()
        self.mobs_draw()
        self.pickups.draw()
        self.powerups.draw()
        self.walls.draw()
        self.obstacles.draw()
