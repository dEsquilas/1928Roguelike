import arcade
import time
from player import Player, Bullet
from rooms import Room
from helpers.Consts import *


from pprint import pprint

# Constants


class Game(arcade.Window):
    def __init__(self):

        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, SCREEN_TITLE)

        self.room = None
        self.player = None
        self.physics_engine = None


        self.sounds = {}

    def setup(self):


        self.room = Room.Room("./assets/scenarios/default.tmx")
        self.player = Player.Player()
        self.physics_engine = arcade.PhysicsEngineSimple(self.player.sprite, self.room.walls)

        # limit framerate

        self.set_update_rate(1 / 60)


    def on_key_press(self, key, modifiers):
        self.player.on_key_press(key, modifiers)

    def on_key_release(self, key, modifiers):
        self.player.on_key_release(key, modifiers)


    def on_update(self, delta_time):

        # updates
        self.room.update()
        self.player.update()
        self.physics_engine.update()

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
