import arcade
import time
from player import Player, Bullet
from rooms import Room
from helpers.Consts import *

class Game(arcade.Window):
    def __init__(self):

        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN_TITLE)

        self.room = None
        self.rooms = []
        self.player = None
        self.physics_player_engine = None
        self.physics_mobs_engines = []
        self.current_room = 1
        self.sounds = {}

    def set_physic_engines(self):
        self.physics_player_engine = arcade.PhysicsEngineSimple(self.player.sprite, self.room.walls)
        self.physics_mobs_engines = []
        for mob in self.room.mobs:
            self.physics_mobs_engines.append(arcade.PhysicsEngineSimple(mob, self.room.walls))

    def update_pyhsics_engines(self):
        self.physics_player_engine.update()
        for engine in self.physics_mobs_engines:
            engine.update()

    def setup(self):

        self.rooms = []
        self.rooms.append(Room.Room("./assets/scenarios/default.tmx", 1))
        self.rooms.append(Room.Room("./assets/scenarios/default2.tmx", 2))

        self.room = self.rooms[self.current_room]
        self.player = Player.Player()
        self.set_physic_engines()

        # limit framerate

        self.set_update_rate(1 / 60)

    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.player.on_key_release(key, modifiers)

    def on_update(self, delta_time):

        # updates

        door = self.room.is_player_on_door(self.player)

        if door:
            self.current_room = door.destination
            for room in self.rooms:
                if room.id == self.current_room:
                    self.room = room
                    break
            self.set_physic_engines()
            self.player.update_from_door(door)

        else:
            self.player.update(self.room.mobs, self.room.powerups)
        self.room.update(self.player)

        self.update_pyhsics_engines()

        if not self.player.is_alive:
            arcade.close_window()

    def on_draw(self):
        self.clear()
        self.room.draw()
        self.player.draw()

def main():
    """Main function"""
    window = Game()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()