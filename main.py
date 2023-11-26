import arcade
import time
from player import Player, Bullet
from mobs import Type1
from helpers.Consts import *
from helpers.SpriteHelper import get_wall_sprites

from pprint import pprint

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

        self.sounds = {}

        # sprites lists
        self.walls = None
        self.mobs = None
        self.bullets = None

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

        self.bullets = arcade.SpriteList()

        self.walls = get_wall_sprites(self)
        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.walls)

        self.sounds["bullet"] = arcade.load_sound("./assets/sounds/shoot.wav")

        self.set_update_rate(1 / 60)


    def on_key_press(self, key, modifiers):
        self.player.is_moving_up = True if key == arcade.key.UP else self.player.is_moving_up
        self.player.is_moving_down = True if key == arcade.key.DOWN else self.player.is_moving_down
        self.player.is_moving_left = True if key == arcade.key.LEFT else self.player.is_moving_left
        self.player.is_moving_right = True if key == arcade.key.RIGHT else self.player.is_moving_right

        self.player.is_attacking = True if key == arcade.key.SPACE else self.player.is_attacking

    def on_key_release(self, key, modifiers):
        self.player.is_moving_up = False if key == arcade.key.UP else self.player.is_moving_up
        self.player.is_moving_down = False if key == arcade.key.DOWN else self.player.is_moving_down
        self.player.is_moving_left = False if key == arcade.key.LEFT else self.player.is_moving_left
        self.player.is_moving_right = False if key == arcade.key.RIGHT else self.player.is_moving_right

        self.player.is_attacking = False if key == arcade.key.SPACE else self.player.is_attacking

    def on_draw(self):
        self.clear()
        self.scene.draw()
        self.bullets.draw()
        self.mobs.draw()

    def check_bullet_collisions(self):

        collisions = []

        for mob in self.mobs:
            current_collisions = arcade.check_for_collision_with_list(mob, self.bullets)
            if current_collisions:
                mob.health -= self.player.attack_dmg
                collisions += current_collisions

        return collisions

    def check_mob_health(self):
        for mob in self.mobs:
            if mob.health <= 0:
                self.mobs.remove(mob)

    def remove_bullets(self, collisions):
        for bullet in self.bullets:
            if bullet.should_remove or bullet in collisions:
                self.bullets.remove(bullet)

    def on_update(self, delta_time):

        if self.player.is_attacking and time.time() - self.player.last_attack_time > self.player.fire_speed:
            self.player.last_attack_time = time.time()
            bullet = Bullet.Bullet((self.player.center_x, self.player.center_y), self.player.direction, self.get_size(), self.sounds["bullet"])
            self.bullets.append(bullet)

        player_collisions = arcade.check_for_collision_with_list(self.player, self.mobs)

        bullet_collisions = self.check_bullet_collisions()
        self.remove_bullets(bullet_collisions)
        self.check_mob_health()

        self.scene.update()
        self.mobs.update()
        self.bullets.update()
        self.physics_engine.update()





def main():
    """Main function"""
    window = Game()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
