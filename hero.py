import random
class Hero:
    """
    This is our hero blueprint.
    
    O=('-'Q)

    Attributes:
        name: The name of our adventurer.
        hp: The current health value.
        strength: The amount of damage the hero can deal.
        (Bonus) defence: A hero's ability to reduce incoming damage.
        (Bonus) special_ability: A unique ability the hero can use.
    """

    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.strength = random.randint(10, 20)
        self.atium_store = random.randint(15,30)
        self.defence = 2

    def burn_atium(self):
        if self.atium_store != 0:
            self.atium_store -= 1
        if self.atium_store == 1:
            print(f"{self.name} has {self.atium_store} second of atium left")
        elif self.atium_store != 0:
            print(f"{self.name} has {self.atium_store} seconds of atium left")
        else:
            print("Vin is out of atium!")

    def strike(self):
        if self.atium_store > 0:
            return self.strength
        else:
            return random.randint(1, self.strength)
    
    def receive_damage(self, damage):
        if self.atium_store == 0:
            if (self.hp - damage) != 0:
                self.hp -= (damage - self.defence)
                print(f"{self.name} takes {damage} damage. Health is now {self.hp}.")
            else:
                self.hp = 0
        else:
            print(f"{self.name} burns atium, dodging the attack and taking no damage")

    def is_alive(self):
        return self.hp > 0