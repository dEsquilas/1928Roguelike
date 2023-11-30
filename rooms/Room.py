import arcade
from helpers.Consts import *

class Room():
    def __init__(self, tile_file):
        super().__init__()

        self.tile_map = arcade.load_tilemap(tile_file, TILE_SCALING, {})
        self.floor = arcade.Scene.from_tilemap(self.tile_map)
        self.mobs = arcade.SpriteList()
        self.pickups = arcade.SpriteList()
        self.powerups = arcade.SpriteList()
        self.walls = self.get_walls()
        self.obstacles = arcade.SpriteList()

    def get_walls(self):
        walls = arcade.SpriteList()
        for sprite in self.floor.get_sprite_list("Walls"):
            walls.append(sprite)
        return walls

    def update(self):
        self.floor.update()
        self.mobs.update()
        self.pickups.update()
        self.powerups.update()
        self.walls.update()
        self.obstacles.update()

    def draw(self):
        self.floor.draw()
        self.mobs.draw()
        self.pickups.draw()
        self.powerups.draw()
        self.walls.draw()
        self.obstacles.draw()

