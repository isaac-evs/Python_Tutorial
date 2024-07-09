# Complex Inheritance excercise

from typing import Any


class Character():

    def __init__(self, name, health):
        self.name = name
        self.health = health
        super().__init__()
    
    def status(self):
        if isinstance(self, Character):
            print(f"{self.name.capitalize()} has {self.health} health")
        else:
            print("invalid")


class Warrior(Character):

    def __init__(self, strength, **kwargs):
        self.strength = strength
        super().__init__(**kwargs)

    def attack(self):
        print(f"{self.name} has attacked dealing {self.strength} damage")
    
    def defend(self):
        print(f"{self.name} is using a shield to block damage")


class Mage(Character):

    def __init__(self, mana, **kwargs):
        self.mana = mana
        super().__init__(**kwargs)
    
    def cast_spell(self):
        if self.mana >= 10:
            print(f"{self.name} has cast a spell dealing 20 damage")
            self.mana -= 10
            print(f"{self.name} has {self.mana} mana left")
        else:
            print(f"Not enough mana, {self.name} needs {10 - self.mana} more mana to cast a spell")
    
    def teleport(self):
        if self.mana >= 20:
            print(f"{self.name} has teleported")
            self.mana -= 20
            print(f"{self.name} has {self.mana} mana left")
        else:
            print(f"Not enough mana, {self.name} needs {20 - self.mana} more mana to teleport")


class BattleMage(Warrior, Mage):

    def __init__(self, name, health, strenght, mana):
        super().__init__(name = name, health = health, strength = strenght, mana = mana)


############################################

# Character
print("\n")
character = Character(
    name = "Tom", 
    health = 100)

character.status()

# Warrior
print("\n")
warrior = Warrior(
    strength = 40, 
    name = "Jane", 
    health = 100)

warrior.status()
warrior.attack()

#Mage
print("\n")
mage = Mage(
    mana = 32, 
    name = "Merlin", 
    health = 100)

mage.status()
mage.cast_spell()
mage.teleport()

#BattleMage
print("\n")
battlemage = BattleMage(name = "Arthur", health = 100, strenght = 40, mana = 55)
battlemage.status()
battlemage.attack()
battlemage.teleport()