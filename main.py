import arcade
from player import Player
from mobs import Type1
from helpers.Consts import *
from helpers.SpriteHelper import get_wall_sprites

# Constants


class Game(arcade.Window):
    def __init__(self):

        width = TILE_WIDTH * TILE_SIZE * TILE_SCALING
        height = TILE_HEIGHT * TILE_SIZE * TILE_SCALING

        super().__init__(width, height, SCREEN_TITLE)
        self.camera = None
        self.scene = None
        self.tile_map = None

        self.gui_camera = None
        self.physics_engine = None

        self.player = None

        # sprites lists
        self.walls = None
        self.mobs = None

        map_name = "./assets/scenarios/default.tmj"

        layer_options = {
        }

        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

    def setup(self):
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        self.camera = arcade.Camera(self.width, self.height)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)


        self.player = Player.Player()
        self.scene.add_sprite("Player", self.player)

        self.mobs = arcade.SpriteList()
        mobType1 = Type1.Type1()
        self.mobs.append(mobType1)

        self.walls = get_wall_sprites(self)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.walls)

    def on_key_press(self, key, modifiers):
        self.player.is_moving_up = True if key == arcade.key.UP else self.player.is_moving_up
        self.player.is_moving_down = True if key == arcade.key.DOWN else self.player.is_moving_down
        self.player.is_moving_left = True if key == arcade.key.LEFT else self.player.is_moving_left
        self.player.is_moving_right = True if key == arcade.key.RIGHT else self.player.is_moving_right

    def on_key_release(self, key, modifiers):
        self.player.is_moving_up = False if key == arcade.key.UP else self.player.is_moving_up
        self.player.is_moving_down = False if key == arcade.key.DOWN else self.player.is_moving_down
        self.player.is_moving_left = False if key == arcade.key.LEFT else self.player.is_moving_left
        self.player.is_moving_right = False if key == arcade.key.RIGHT else self.player.is_moving_right

    def on_draw(self):
        self.clear()
        self.scene.draw()
        self.mobs.draw()

    def on_update(self, delta_time):
        self.scene.update()
        self.mobs.update()
        self.physics_engine.update()





def main():
    """Main function"""
    window = Game()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
