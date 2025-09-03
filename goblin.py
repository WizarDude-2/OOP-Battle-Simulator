import random

class Goblin:
    def __init__(self, name):
        self.name = name
        self.health = 150
        self.attack_power = random.randint(5, 10)

    def attack(self):
        return random.randint(1, self.attack_power)

    def take_damage(self, damage):
        if (self.health - damage) != 0:
            self.health -= damage
        else:
            self.health = 0
        print(f"{self.name} takes {damage} damage. Health is now {self.health}.")

    def is_alive(self):
        return self.health > 0
