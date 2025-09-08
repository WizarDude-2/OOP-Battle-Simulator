import random
class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.strength = random.randint(10, 20)
        self.atium_store = random.randint(56,120)
        self.defence = 5

    def burn_atium(self):
        if self.atium_store != 0:
            self.atium_store -= 1
        if self.atium_store == 1:
            print(f"{self.name} has {self.atium_store} second of atium left")
        elif self.atium_store != 0:
            print(f"{self.name} has {self.atium_store} seconds of atium left")
        else:
            print(f"{self.name} is out of atium!")

    def strike(self):
        if self.atium_store > 0:
            return self.strength
        else:
            return random.randint(1, self.strength)
    
    def receive_damage(self, damage):
        if self.atium_store == 0:
            if not((self.hp - damage) > self.hp):
                self.hp -= abs(damage - self.defence)
                print(f"{self.name} takes {damage} damage. Health is now {self.hp}.")
        else:
            print(f"{self.name} burns atium, dodging the attack and taking no damage")

    def is_alive(self):
        return self.hp > 0