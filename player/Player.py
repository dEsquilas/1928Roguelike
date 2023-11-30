import arcade
import time
from helpers.Consts import *
from helpers.Attributes import Attributes
from helpers.Sounds import ssounds
from player import PlayerSprite, Bullet

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

        self.attr = Attributes(100, 5, 0.1, 10)

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
            bullet = Bullet.Bullet((self.sprite.center_x, self.sprite.center_y), self.facing)
            self.bullets.append(bullet)

    def check_bullets_to_remove(self):
        for bullet in self.bullets:
            if bullet.should_remove:
                self.bullets.remove(bullet)

    def check_player_damage_collisions(self, mobs):
        for mob in mobs:
            if arcade.check_for_collision(self.sprite, mob) and time.time() - self.last_hit_time > IFRAMES:
                self.attr.set("health", self.attr.get("health") - mob.attr.get("attack_dmg"))
                self.last_hit_time = time.time()
                ssounds.play("ouch")
                print(self.attr.get("health"))

        if self.attr.get("health") <= 0:
            self.is_alive = False


    def update(self, mobs):

        self.fire()

        self.check_bullets_to_remove()
        self.check_player_damage_collisions(mobs)

        self.sprite.update(self.is_moving, self.attr.get("speed"))
        self.bullets.update()

    def draw(self):
        self.bullets.draw()
        self.sprite.draw()



