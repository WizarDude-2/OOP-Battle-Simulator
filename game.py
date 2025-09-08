import random
from koloss import Koloss
from hero import Hero
from stInq import stInq

def main():
    print("The Siege of Luthadel has begun")

    # Create a hero
    hero = Hero("Vin")

    # Create goblins ༼ ºل͟º ༽ ༼ ºل͟º ༽ ༼ ºل͟º ༽
    goblins = [Koloss(f"Koloss {i+1}") for i in range(5)]

    # Keep track of how many goblins were defeated
    defeated_goblins = 0
    roundCount = 0

    # Battle Loop 
    while hero.is_alive() and any(goblin.is_alive() for goblin in goblins):
        print("\nNew Round!")
        # Hero's turn to attack
        target_goblin = random.choice([goblin for goblin in goblins if goblin.is_alive()])
        damage = hero.strike()
        print(f"{hero.name} attacks {target_goblin.name} for {damage} damage!")
        target_goblin.take_damage(damage)

        # Check if the target goblin was defeated
        if not target_goblin.is_alive():
            defeated_goblins += 1
            print(f"{target_goblin.name} has been defeated!")

        # Goblins' turn to attack
        for goblin in goblins:
            if goblin.is_alive():
                damage = goblin.attack()
                print(f"{goblin.name} attacks {hero.name} for {damage} damage!")
                hero.receive_damage(damage)
        hero.burn_atium()
        roundCount += 1
        input(f"Press any key to continue: ")
    # Determine outcome

    if hero.is_alive():
        print(f"{roundCount} rounds to kill koloss")
        print(f"\n{hero.name} has shattered the koloss force. A cloaked figure steps from the mist... a Steel Inquisitor joins the battle.")
        input(f"Press any key to continue: ")
        boss = stInq("Steel Inquisitor")
        roundCount = 0
        while hero.is_alive() and boss.is_alive():
            print("\nNew Round!")
            damage = hero.strike()
            print(f"{hero.name} attacks {boss.name} for {damage} damage!")
            boss.take_damage(damage)
            if not boss.is_alive():
                print(f"{boss.name} has been defeated!")
            
            if boss.is_alive():
                damage = boss.attack()
                print(f"{boss.name} attacks {hero.name} for {damage} damage!")
                hero.receive_damage(damage)

            hero.burn_atium()
            boss.burn_atium()
            roundCount += 1
            input(f"Press any key to continue: ")
        if hero.is_alive():
            print(f"\n{hero.name} has defeated the Inquisitor. Luthadel stands.")
        else:
            print(f"\nThe Heir of the Survivor has succumbed to the Inquisitor's overwhelming allomantic might. Luthadel has fallen.")
    else:
        print(f"\nThe Heir of the Survivor has succumbed to the koloss horde. Luthadel has fallen.")

    # Final tally of goblins defeated
    print(f"\nTotal koloss defeated: {defeated_goblins} / {len(goblins)}")

if __name__ == "__main__":
    main()