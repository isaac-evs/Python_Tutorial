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
            print(f"{self.name} has ascended 1 level")
        print(f"{self.name} is now level {self.level}")
        

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

    def __init__(self, damage, name, value):
        self.damage = damage
        super().__init__(name, value)

    def use(self, user, target):
        target.health -= self.damage
        print(f"{user.name} has dealth {self.damage} damage with a {self.name} to {target.name}")
        if target.is_alive() == True:
            print(f"{target.name.capitalize()} actual health is {target.health}")
        else:
            print(f"{target.name.capitalize()} is dead")
            user.gain_experience(50)


class Potion(Item):

    def __init__(self, healing_ammount, name, value):
        self.healing_ammount = healing_ammount
        super().__init__(name, value)
    
    def use(self, target):
        target.health += self.healing_ammount
        print(f"{target.name} has used {self.name}, it has replenished {self.healing_ammount} health")
        print(f"{target.name} now has {target.health} health")
    

##########################################

player = PlayerCharacter(
    level = 5, 
    experience = 12, 
    name = "Tom", 
    health = 80)

npc = NonPlayerCharacter(
    dialogue = "Is dangerous to go alone! take this", 
    name = "old man", 
    health = 100)

weapon = Weapon(
    damage = 120,
    name = "sword",
    value = 1)

potion = Potion(
    healing_ammount = 10,
    name = "blue potion",
    value = 2)

#####################################################

# player uses weapon on npc 
weapon.use(user = player, target = npc)

# player uses potion to heal himself'
potion.use(target = player)

