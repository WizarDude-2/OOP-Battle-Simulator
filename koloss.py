import random
from enemy import Enemy

class Koloss(Enemy):
    def __init__(self, name):
        self.age = random.randint(10,20)
        self.health = 10*self.age
        self.attack_power = random.randint(1, self.age)
        self.name = name
        print(self.name)
