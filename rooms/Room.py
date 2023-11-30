import arcade
from mobs.MobBase import MobBase
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

        mobs1 = MobBase((250, 100))
        mobs2 = MobBase((300, 150))

        self.mobs.append(mobs1)
        self.mobs.append(mobs2)

    def get_walls(self):
        walls = arcade.SpriteList()
        for sprite in self.floor.get_sprite_list("Walls"):
            walls.append(sprite)
        return walls

    def mobs_update(self, player_sprite):
        for mob in self.mobs:
            mob.custom_update(player_sprite)

    def mobs_draw(self):
        for mob in self.mobs:
            mob.draw()

    def update(self, player):
        self.floor.update()
        self.mobs_update(player.sprite)
        self.pickups.update()
        self.powerups.update()
        self.walls.update()
        self.obstacles.update()

    def draw(self):
        self.floor.draw()
        self.mobs_draw()
        self.pickups.draw()
        self.powerups.draw()
        self.walls.draw()
        self.obstacles.draw()

