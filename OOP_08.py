# Simple Inheritance excercise

class Character:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

class PlayerCharacter(Character):

    def __init__(self, level, experience, name, health):
        self.level = level
        self.experience = experience
        super().__init__(name, health)

    def gain_experience(self, exp):
        self.experience += exp
        while self.experience >= 15:
            self.level += 1
            self.experience -= 15

class NonPlayerCharacter(Character):

    def __init__(self, dialogue, name, health):
        self.dialogue = dialogue
        super().__init__(name, health)

    def speak(self):
        print(f"{self.name}: {self.dialogue}")

######################################

class Item:

    def __init__(self, name, value):
        self.name = name
        self.value = value


class Weapon(Item):

    def __init__(self, damage, name, value)
        self.damage = damage
        super().__init__(name, value)

    def use(self, target)
        sel.
