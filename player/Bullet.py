import arcade
from helpers.Consts import *
from helpers.Sounds import ssounds

class Bullet(arcade.Sprite):
    def __init__(self, origin, direction, attack_dmg=1):
        super().__init__()
        self.texture = arcade.load_texture("./assets/sprites/bullet.png")
        self.scale = 2
        self.center_x = origin[0]
        self.center_y = origin[1]
        self.speed = 10
        self.attack_dmg = attack_dmg
        self.max_distance = 100 * TILE_SCALING
        self.origin = origin
        self.limits = (WINDOW_WIDTH, WINDOW_HEIGHT)
        self.should_remove = False

        self.direction = [
            1 if direction == UP else 0,
            1 if direction == DOWN else 0,
            1 if direction == LEFT else 0,
            1 if direction == RIGHT else 0]

        ssounds.play("bullet")

    def custom_update(self, walls):

        super().update()

        self.center_x += self.speed * (self.direction[3] - self.direction[2])
        self.center_y += self.speed * (self.direction[0] - self.direction[1])

        current_distance = abs(self.center_x - self.origin[0]) + abs(self.center_y - self.origin[1])

        if self.center_x < 0 or self.center_x > self.limits[0] or self.center_y < 0 or self.center_y > self.limits[1] or current_distance >= self.max_distance:
            self.should_remove = True

        for wall in walls:
            if arcade.check_for_collision(self, wall):
                self.should_remove = True
                break

