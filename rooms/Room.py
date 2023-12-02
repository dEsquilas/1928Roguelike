import copy
import arcade
from helpers.Attributes import Attributes
from helpers.Consts import *
from mobs.MobBase import MobBase
from powerups.PowerUpBase import PowerUpBase
from rooms.Door import Door
from rooms.BlockItem import BlockItem

class Room():
    def __init__(self, tile_file, id):
        super().__init__()

        self.tile_map = arcade.load_tilemap(tile_file, TILE_SCALING, {})
        self.floor = arcade.Scene.from_tilemap(self.tile_map)
        self.mobs = []
        self.pickups = arcade.SpriteList()
        self.powerups = arcade.SpriteList()
        self.obstacles = arcade.SpriteList()
        self.doors = arcade.SpriteList()
        self.id = id

        # add elements

        door1 = Door(1, 1)
        door2 = Door(2, 2)
        door3 = Door(3, 1)
        door4 = Door(4, 2)

        self.doors.append(door1)
        self.doors.append(door2)
        self.doors.append(door3)
        self.doors.append(door4)

        attr = Attributes(100, 0.5, 0.1, 10)

        mobs1 = MobBase((250, 100), copy.deepcopy(attr), 1)
        mobs2 = MobBase((300, 150), copy.deepcopy(attr), 2)

        self.mobs.append(mobs1)
        self.mobs.append(mobs2)

        powerup = PowerUpBase((450, 200))
        self.powerups.append(powerup)

        obstacle1 = BlockItem((100, 100))
        obstacle2 = BlockItem((150, 100))
        self.obstacles.append(obstacle1)
        self.obstacles.append(obstacle2)

        self.walls = self.get_walls()

    def get_walls(self):
        walls = arcade.SpriteList()
        for sprite in self.floor.get_sprite_list("Walls"):
            walls.append(sprite)

        for obstacles in self.obstacles:
            walls.append(obstacles)

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
        self.powerups.update()
        for powerup in self.powerups:
            if powerup.should_remove:
                self.powerups.remove(powerup)

    def is_player_on_door(self, player):
        for id, door in enumerate(self.doors):
            if arcade.check_for_collision(player.sprite, door):
                return door
        return False

    def update(self, player):
        self.floor.update()
        self.mobs_update(player)
        self.pickups.update()
        self.powerups_update()
        self.walls.update()
        self.obstacles.update()
        self.doors.update()

    def draw(self):
        self.floor.draw()
        self.mobs_draw()
        self.pickups.draw()
        self.powerups.draw()
        self.walls.draw()
        self.obstacles.draw()
        self.doors.draw()

