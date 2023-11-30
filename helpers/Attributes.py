class Attributes:
    def __init__(self, health, speed, fire_speed, attack_dmg):
        super().__init__()
        self.health = health
        self.speed = speed
        self.fire_speed = fire_speed
        self.attack_dmg = attack_dmg

    def get(self, attr):
        return self.__dict__[attr]

    def set(self, attr, value):
        self.__dict__[attr] = value
