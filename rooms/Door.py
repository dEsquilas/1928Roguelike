import arcade
from helpers.Consts import *
from helpers.Sounds import ssounds

class Door(arcade.Sprite):
    def __init__(self, type=1, destination=-1):
        super().__init__()

        self.destination = destination
        self.type = type
        self.scale = TILE_SCALING
        self.status = 0

        if type == 1:
            self.texture_closed = arcade.load_texture("./assets/sprites/door_top.png")
            self.texture_opened = arcade.load_texture("./assets/sprites/door_top_opened.png")
            self.center_x = WINDOW_WIDTH / 2
            self.center_y = WINDOW_HEIGHT - TILE_SIZE * 1.75
        elif type == 2:
            self.texture_closed = arcade.load_texture("./assets/sprites/door_lateral.png")
            self.texture_opened = arcade.load_texture("./assets/sprites/door_lateral_opened.png")
            self.center_x = WINDOW_WIDTH - TILE_WIDTH / 2
            self.center_y = WINDOW_HEIGHT / 2
        elif type == 3:
            self.texture_closed = arcade.load_texture("./assets/sprites/door_bottom.png")
            self.texture_opened = arcade.load_texture("./assets/sprites/door_bottom_opened.png")
            self.center_x = WINDOW_WIDTH / 2
            self.center_y = TILE_SIZE / 2
        elif type == 4:
            self.texture_closed = arcade.load_texture("./assets/sprites/door_lateral.png", flipped_horizontally=True)
            self.texture_opened = arcade.load_texture("./assets/sprites/door_lateral_opened.png", flipped_horizontally=True)
            self.center_y = WINDOW_HEIGHT / 2
            self.center_x = self.width / 2

        self.texture = self.texture_closed

    def unlock(self):
        self.texture = self.texture_opened
        ssounds.play("door_open")
        self.status = 1


    def lock(self):
        self.texture = self.texture_closed
        ssounds.play("door_close")
        self.status = 0
