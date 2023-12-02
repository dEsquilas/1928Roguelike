import arcade

class Sounds():
    def __init__(self):
        super().__init__()
        self.sounds = {}

        current_sounds = [
            ("crash", "mp3"),
            ("mob_dead", "mp3"),
            ("ouch", "mp3"),
            ("pop", "wav"),
            ("bullet", "wav"),
            ("powerup", "mp3")
        ]

        for sound in current_sounds:
            self.load(sound[0 ], "./assets/sounds/" + sound[0] + "." + sound[1])

    def play(self, name):
        arcade.play_sound(self.sounds[name])

    def load(self, name, path):
        self.sounds[name] = arcade.load_sound(path)


ssounds = Sounds()