import arcade
from helpers.Consts import *

class Door(arcade.Sprite):
    def __init__(self, type=1, destination=-1):
        super().__init__()

        self.destination = destination
        self.type = type
        self.scale = TILE_SCALING

        if type == 1:
            self.texture = arcade.load_texture("./assets/sprites/door.jpg")
            self.center_x = WINDOW_WIDTH / 2
            self.center_y = WINDOW_HEIGHT - self.height / 2
        elif type == 2:
            self.texture = arcade.load_texture("./assets/sprites/door_lateral.png")
            self.center_x = WINDOW_WIDTH - self.width / 2
            self.center_y = WINDOW_HEIGHT / 2
        elif type == 3:
            self.texture = arcade.load_texture("./assets/sprites/door_lateral.png")
            self.center_x = WINDOW_WIDTH / 2
            self.center_y = self.height / 2
        elif type == 4:
            self.texture = arcade.load_texture("./assets/sprites/door_lateral.png")
            self.center_y = WINDOW_HEIGHT / 2
            self.center_x = self.width / 2


