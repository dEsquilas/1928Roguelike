import arcade
import time
from player import Player, Bullet
from mobs import Type1
from powerups import PowerUp1
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
        self.player_sprites = None
        self.walls_sprites = None
        self.mobs_sprites = None
        self.items_sprites = None
        self.bullets_sprites = None

        map_name = "./assets/scenarios/default.tmj"

        layer_options = {
        }

        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

    def setup(self):
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        self.camera = arcade.Camera(self.width, self.height)
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        # define sprites lists

        self.bullets_sprites = arcade.SpriteList()
        self.player_sprites = arcade.SpriteList()
        self.mobs_sprites = arcade.SpriteList()
        self.bullets_sprites = arcade.SpriteList()
        self.items_sprites = arcade.SpriteList()
        self.walls_sprites = get_wall_sprites(self)

        # append initial elements to sprites lists

        self.player = Player.Player()
        self.player_sprites.append(self.player)

        mobType1 = Type1.Type1((200, 200))
        self.mobs_sprites.append(mobType1)

        powerUp1 = PowerUp1.PowerUp1((100, 100))
        self.items_sprites.append(powerUp1)


        self.physics_engine = arcade.PhysicsEngineSimple(self.player, self.walls_sprites)

        # sounds

        self.sounds["bullet"] = arcade.load_sound("./assets/sounds/shoot.wav")
        self.sounds["mob_dead"] = arcade.load_sound("./assets/sounds/mob_dead.mp3")
        self.sounds["ouch"] = arcade.load_sound("./assets/sounds/ouch.mp3")
        self.sounds["crash"] = arcade.load_sound("./assets/sounds/crash.mp3")
        self.sounds["pickup_powerup"] = arcade.load_sound("./assets/sounds/pop.wav")

        # limit framerate

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


    def check_bullet_mobs_collisions(self):

        collisions = []

        for mob in self.mobs_sprites:
            current_collisions = arcade.check_for_collision_with_list(mob, self.bullets_sprites)
            if current_collisions:
                mob.health -= self.player.attr["attack_dmg"]
                collisions += current_collisions

        return collisions

    def check_mob_health(self):
        for mob in self.mobs_sprites:
            if mob.health <= 0:
                self.mobs_sprites.remove(mob)
                arcade.play_sound(self.sounds["mob_dead"])

    def check_mob_player_collisions(self):
        collisions = arcade.check_for_collision_with_list(self.player, self.mobs_sprites)
        if len(collisions) and time.time() - self.player.last_damage_time > 0.2:
            arcade.play_sound(self.sounds["ouch"])
            self.player.attr["health"] -= collisions[0].attack_dmg
            self.player.last_damage_time = time.time()
        return collisions

    def check_player_items_collisions(self):
        collisions = arcade.check_for_collision_with_list(self.player, self.items_sprites)
        if len(collisions):
            collisions[0].apply_effect(self.player)
            arcade.play_sound(self.sounds["pickup_powerup"])
            self.items_sprites.remove(collisions[0])

    def check_player_health(self):
        if self.player.attr["health"] <= 0:
            arcade.play_sound(self.sounds["crash"])
            self.player_sprites.remove(self.player)
            self.player = None

    def remove_bullets(self, collisions):
        for bullet in self.bullets_sprites:
            if bullet.should_remove or bullet in collisions:
                self.bullets_sprites.remove(bullet)


    def fire_bullets(self):
        if self.player.is_attacking and time.time() - self.player.last_attack_time > self.player.attr["fire_speed"]:
            self.player.last_attack_time = time.time()
            bullet = Bullet.Bullet((self.player.center_x, self.player.center_y), self.player.direction, self.get_size(), self.sounds["bullet"])
            self.bullets_sprites.append(bullet)

    def custom_mobs_sprites_update(self, player):
        for mob in self.mobs_sprites:
            mob.update(player)

    def on_update(self, delta_time):

        bullet_collisions = self.check_bullet_mobs_collisions()
        self.remove_bullets(bullet_collisions)
        self.check_mob_health()

        if self.player:
            self.fire_bullets()
            self.check_mob_player_collisions()
            self.check_player_health()
            self.check_player_items_collisions()


        # updates
        self.scene.update()
        self.player_sprites.update()
        self.custom_mobs_sprites_update(self.player)
        self.bullets_sprites.update()
        self.physics_engine.update()

    def on_draw(self):
        self.clear()
        self.scene.draw()
        self.player_sprites.draw()
        self.items_sprites.draw()
        self.bullets_sprites.draw()
        self.mobs_sprites.draw()





def main():
    """Main function"""
    window = Game()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
