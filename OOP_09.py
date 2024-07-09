# Complex Inheritance excercise

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

class Player():

    def __init__(self, level, experience, **kwargs):
        self.level = level
        self.experience = experience
        super().__init__(**kwargs)

    def gain_experience(self, exp):
        self.experience += exp
        while self.experience >= 15:
            self.level += 1
            self.experience -= 15
            print(f"{self.name} has ascended 1 level")
        print(f"{self.name} is now level {self.level}")
        

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


class BattleMage(Player, Warrior, Mage):

    def __init__(self, level, experience, name, health, strength, mana):
        super().__init__(level = level, experience = experience, name = name, health = health, strength = strength, mana = mana,)


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
print(BattleMage.mro())
print("\n")
battlemage = BattleMage(name = "Arthur", health = 100, strength = 40, mana = 55, level = 5, experience = 12)
battlemage.status()
battlemage.attack()
battlemage.teleport()
battlemage.gain_experience(32)