# Simple Inheritance

class Monster:

    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
    
    def attack(self, ammount):
        print("The monster has attacked")
        print(f"{ammount} damage was dealt")
        self.energy -= 20
    
    def move(self, speed):
        print("The monster has moved")
        print(f"It has a speed of {speed}")


class Shark(Monster):

    def __init__(self,speed, health, energy):
        #Monster.__init__(self,health,energy)
        super().__init__(health, energy)
        self.speed = speed
    
    def bite(self):
        print("The shark has bitten")
        self.energy -= 50
    
    def move(self):
        print("The shark has moved")
        print(f"It has a speed of {self.speed}")

#######################################################

class Scorpion(Monster):

    def __init__(self, poison_dmg, health, energy):
        self.poison_dmg = poison_dmg
        super().__init__(health, energy)
    
    def attack(self):
        print("The scorpion has attacked")
        print(f"{self.poison_dmg} damage was dealth")
        self.energy -= 10


scorpion = Scorpion(poison_dmg = 10, health = 60, energy = 40)

scorpion.attack()
print(scorpion.energy)