import arcade
from helpers.Consts import *

class HPHud(arcade.Sprite):
    def __init__(self, current_hp, max_hp):
        super().__init__()
        self.texture = arcade.load_texture("./assets/sprites/hp_hud.png")
        self.scale = TILE_SCALING
        self.center_x = TILE_SCALING * 15
        self.center_y = WINDOW_HEIGHT - TILE_SCALING * 30

        self.current_hp = current_hp
        self.max_hp = max_hp

    def custom_update(self, current_hp):
        super().update()
        self.current_hp = current_hp


    def draw(self):
        super().draw()

        hp_bar_min = 0
        hp_bar_max = TILE_SCALING * 41

        hp_bar_width = TILE_SCALING * 12 + 1  # sprite is odd
        hp_bar_height = ((self.current_hp / self.max_hp) * hp_bar_max)

        hp_bar_bottom = self.bottom + hp_bar_height / 2 + (TILE_SCALING * 4)

        # Dibuja un rectángulo en la parte inferior del sprite.
        arcade.draw_rectangle_filled(self.center_x, hp_bar_bottom,
                                        hp_bar_width,
                                        hp_bar_height,
                                        color=(55, 165, 88))