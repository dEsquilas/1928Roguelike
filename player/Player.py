import arcade
import copy
import time
from helpers.Consts import *
from helpers.Attributes import Attributes
from helpers.Sounds import ssounds
from player import PlayerSprite, Bullet, HPHud

class Player():
    def __init__(self):
        super().__init__()

        self.sprite = PlayerSprite.PlayerSprite()
        self.bullets = arcade.SpriteList()
        self.is_alive = True
        self.is_attacking = 0
        self.last_attack_time = 0
        self.last_hit_time = 0
        self.facing = UP

        self.attr = Attributes(100, 5, 0.3, 10)

        self.current_hp = self.attr.get("health")
        self.hp_hud = HPHud.HPHud(self.current_hp, self.attr.get("health"))

        self.is_moving = {}
        for direction in DIRECTIONS:
            self.is_moving[direction] = False

    def on_key_press(self, key, modifiers):

        for direction in DIRECTIONS:
            self.is_moving[direction] = True if key == DIRECTION_KEYS[direction] else self.is_moving[direction]
            if self.is_moving[direction]:
                self.facing = direction

        self.is_attacking = True if key == arcade.key.SPACE else self.is_attacking

    def on_key_release(self, key, modifiers):

        for direction in DIRECTIONS:
            self.is_moving[direction] = False if key == DIRECTION_KEYS[direction] else self.is_moving[direction]

        self.is_attacking = False if key == arcade.key.SPACE else self.  is_attacking

    def fire(self):
        if self.is_attacking and time.time() - self.last_attack_time > self.attr.get("fire_speed"):
            self. last_attack_time = time.time()
            bullet = Bullet.Bullet((self.sprite.center_x, self.sprite.center_y), self.facing, self.attr.get("attack_dmg"))
            self.bullets.append(bullet)

    def check_bullets_to_remove(self):
        for bullet in self.bullets:
            if bullet.should_remove:
                self.bullets.remove(bullet)

    def check_player_damage_collisions(self, mobs):
        for mob in mobs:
            if arcade.check_for_collision(self.sprite, mob) and time.time() - self.last_hit_time > IFRAMES:
                self.current_hp -= mob.attr.get("attack_dmg")
                self.last_hit_time = time.time()
                ssounds.play("ouch")

        if self.current_hp <= 0:
            self.is_alive = False

    def check_bullet_mobs_collisions(self, mobs):

        for mob in mobs:
            for bullet in self.bullets:
                if arcade.check_for_collision(mob, bullet):
                    mob.attr.set("health", mob.attr.get("health") - self.attr.get("attack_dmg"))
                    bullet.should_remove = True

    def check_player_powerup_collisions(self, powerups):
        for powerup in powerups:
            if arcade.check_for_collision(self.sprite, powerup):
                powerup.apply_effect(self)
                powerup.should_remove = True
                ssounds.play("powerup")

    def check_player_pickup_collisions(self, pickups):
        for pickup in pickups:
            if arcade.check_for_collision(self.sprite, pickup):
                pickup.apply_effect(self)
                pickup.should_remove = True
                if pickup.sound:
                    ssounds.play(pickup.sound)

    def bullets_update(self, walls):
        for bullet in self.bullets:
            bullet.custom_update(walls)

    def update(self, room):

        self.fire()
        self.check_bullet_mobs_collisions(room.mobs)
        self.check_player_powerup_collisions(room.powerups)
        self.check_player_pickup_collisions(room.pickups)

        self.check_bullets_to_remove()
        self.check_player_damage_collisions(room.mobs)

        self.sprite.update(self.is_moving, self.attr.get("speed"))
        self.bullets_update(room.walls)

        self.hp_hud.custom_update(self.current_hp)

    def update_from_door(self, door):

        if door.type == 1:
            self.sprite.center_x = WINDOW_WIDTH / 2
            self.sprite.center_y = self.sprite.height / 2 + TILE_SIZE * TILE_SCALING
        elif door.type == 2:
            self.sprite.center_x = self.sprite.width / 2 + TILE_SIZE * TILE_SCALING
            self.sprite.center_y = WINDOW_HEIGHT / 2
        elif door.type == 3:
            self.sprite.center_x = WINDOW_WIDTH / 2
            self.sprite.center_y = WINDOW_HEIGHT - self.sprite.height / 2 - (TILE_SIZE * TILE_SCALING * 2) # this tile has 2x height
        elif door.type == 4:
            self.sprite.center_y = WINDOW_HEIGHT / 2
            self.sprite.center_x = WINDOW_WIDTH - self.sprite.width / 2 - TILE_SIZE * TILE_SCALING

    def draw(self):
        self.bullets.draw()
        self.sprite.draw()
        self.hp_hud.draw()



