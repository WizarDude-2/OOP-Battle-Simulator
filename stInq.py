from enemy import Enemy
import random

class stInq(Enemy):
    def __init__(self, name):
        self.health = 200
        self.attack_power = random.randint(10,20)
        self.atium_store = random.randint(30,60)
        self.name = name

    def burn_atium(self):
        if self.atium_store != 0:
            self.atium_store -= 1
        if self.atium_store == 1:
            print(f"{self.name} has {self.atium_store} second of atium left")
        elif self.atium_store != 0:
            print(f"{self.name} has {self.atium_store} seconds of atium left")
        else:
            print(f"{self.name} is out of atium!")

    def attack(self):
        if self.atium_store > 0:
            return self.attack_power
        else:
            return random.randint(1, self.attack_power)
    
    def take_damage(self, damage):
        if self.atium_store == 0:
            if not((self.health - damage) > self.health):
                self.health -= damage
                print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
        else:
            print(f"{self.name} burns atium, dodging the attack and taking no damage")
