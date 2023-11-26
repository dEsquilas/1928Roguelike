import arcade
from helpers.Consts import *

class Bullet(arcade.Sprite):
    def __init__(self, origin, direction, limits):
        super().__init__()
        self.texture = arcade.load_texture("./assets/sprites/bullet.png")
        self.scale = 2
        self.center_x = origin[0]
        self.center_y = origin[1]
        self.speed = 10
        self.max_distance = 200 * TILE_SCALING
        self.origin = origin
        self.limits = limits
        self.should_remove = False

        self.direction = [
            1 if direction == D_UP else 0,
            1 if direction == D_DOWN else 0,
            1 if direction == D_LEFT else 0,
            1 if direction == D_RIGHT else 0]



    def update(self):
        self.center_x += self.speed * (self.direction[3] - self.direction[2])
        self.center_y += self.speed * (self.direction[0] - self.direction[1])

        current_distance = abs(self.center_x - self.origin[0]) + abs(self.center_y - self.origin[1])

        if self.center_x < 0 or self.center_x > self.limits[0] or self.center_y < 0 or self.center_y > self.limits[1] or current_distance >= self.max_distance:
            self.should_remove = True



