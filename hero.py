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
        self.health = 150
        self.attack_power = random.randint(8, 10)
        self.atium_store = random.randint(0,4)
        self.defence = 2

    def burn_atium(self):
        self.atium_store -= 1

    def strike(self):
        if self.atium >= 0:
            return self.attack_power
        else:
            return random.randint(1, self.attack_power)
    
    def take_damage(self, damage):
        if self.atium < 0:
            self.health -= (damage - self.defense)
            print(f"{self.name} takes {damage} damage. Health is now {self.health}.")
        else:
            print(f"{self.name} burns atium, dodging the attack and taking no damage")

    def is_alive(self):
        return self.health > 0