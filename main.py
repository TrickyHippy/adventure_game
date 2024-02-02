from numpy import random

def monster(health, level, armor, power):
    monster_index = random.randint(10)
    monster_names = [
    "Goblin",
    "Skeleton",
    "Orc",
    "Harpy",
    "Cyclops",
    "Dragon",
    "Kraken",
    "Hydra",
    "Behemoth",
    "Demonlord"
]
    monster_hp = 10*(monster_index+1)
    monster_power = 1 + 2*monster_index + random.randint(5)
    print(f"You encounter a {monster_names[monster_index]}.")
    while monster_hp > 0:
        x = input("""\n
For fighting type; fight.
For running type; escape.\n
""")
        if x == "fight":
            monster_hp -= level+power+random.randint(5)
            if monster_power > armor:
                health -= monster_power-armor
            if health <= 0:
                return health, monster_names[monster_index], monster_hp
                break
            print(f"Your HP are: {health}\nThe {monster_names[monster_index]} HP are: {monster_hp}")
        elif x == "escape":
            health -= monster_power
            break
        else:
            print("Invalid input.")
    return health, monster_names[monster_index], monster_hp

def AdventureGame():
    healing_potions = 0
    power = 1
    armor = 0
    health = 50
    level = 1

    while True:
        x = input("""\n
Hello Adventurer:
If you want to search the dungeon for items or monsters: type; search.
If you want to use a healing potion: type; heal.
If you want to show stats: type; stats\n
""")
        if x == "search":
            y = random.randint(5)
            if y == 0 or y == 1:
                healing_potions += 1
                print("You found a healing potion.")
            elif y == 2:
                power += 2
                print("You found a power rune.")
            elif y == 3:
                armor += 1
                print("You found an armor rune.")
            else:
                battle, monster_name, monster_health = monster(health, level, armor, power)
                health = battle
                if health <= 0:
                    print(f"You got killed by the {monster_name}.")
                    break
                else:
                    if monster_name == "Demonlord" and monster_health <= 0:
                        print(f"You killed the {monster_name} and therefore win the game")
                        break
                    if monster_health <= 0:
                        level += 1
                        print(f"You earned a level up by slaying the {monster_name}.")
        elif x == "heal":
            if healing_potions > 0:
                healing_potions -= 1
                health = 50
            else:
                print("You have no potions.")
        elif x == "stats":
            print(f"""
level = {level}
health = {health}
power = {power}
armor = {armor}
potions = {healing_potions}
""")

        else:
            print("invalid input.")

AdventureGame()
