import copy
import arcade
from helpers.Attributes import Attributes
from helpers.Consts import *
from mobs.MobBase import MobBase
from pickups import Heart
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
        self.is_opened = 0
        self.physics_engine_changed = False

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

        if id == 1:
            obstacle1 = BlockItem((100, 100))
            obstacle2 = BlockItem((150, 100))
            self.obstacles.append(obstacle1)
            self.obstacles.append(obstacle2)

            pickup1 = Heart.Heart((200, 100))
            self.pickups.append(pickup1)

    def set_walls(self):
        self.walls = self.get_walls()

    def get_walls(self):
        walls = arcade.SpriteList()
        for sprite in self.floor.get_sprite_list("Walls"):
            walls.append(sprite)

        for obstacles in self.obstacles:
            walls.append(obstacles)

        if self.is_opened == 0:
            for door in self.doors:
                if door.status == 0:
                    walls.append(door)

        return walls

    def mobs_update(self, player):
        for mob in self.mobs:
            mob.custom_update(player)
            if mob.should_remove:
                self.mobs.remove(mob)

        if len(self.mobs) == 0 and self.is_opened == 0:
            self.is_opened = 1
            self.unlock_doors()

    def mobs_draw(self):
        for mob in self.mobs:
            mob.draw()

    def powerups_update(self):
        self.powerups.update()
        for powerup in self.powerups:
            if powerup.should_remove:
                self.powerups.remove(powerup)

    def pickups_update(self):
        self.pickups.update()
        for pickup in self.pickups:
            if pickup.should_remove:
                self.pickups.remove(pickup)

    def is_player_on_door(self, player):
        for id, door in enumerate(self.doors):
            if arcade.check_for_collision(player.sprite, door):
                return door
        return False

    def unlock_doors(self):
        for door in self.doors:
            door.unlock()
        self.is_opened = 1
        self.physics_engine_changed = True

    def lock_doors(self):
        for door in self.doors:
            door.lock()
        self.is_opened = 0
        self.physics_engine_changed = True

    def is_physic_engine_changed(self):

        if self.physics_engine_changed:
            self.physics_engine_changed = False
            return True

        return False

    def update(self, player):
        self.floor.update()
        self.mobs_update(player)
        self.pickups_update()
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

