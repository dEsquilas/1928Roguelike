import arcade

def get_wall_sprites(self):
    not_map_sprites = [
        "Floor",
    ]

    walls = arcade.SpriteList()

    for sprite_list_name in self.room.name_mapping:
        if sprite_list_name not in not_map_sprites:
            for sprite in self.room.name_mapping[sprite_list_name]:
                walls.append(sprite)

    return walls