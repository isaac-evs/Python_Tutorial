# Dunder methods

class Monster:

    #attributes
    health = 90
    energy = 40

    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    #methods
    def attack(self, amount):
        print("The monster has attacked")
        print(f"{amount} demage was dealt")
        self.energy -=10
        print(self.energy)

    def move(self, speed):
        print("The monster has moved")
        print(f"moving at {speed} km/h")


monster1 = Monster(10,20)
monster2 = Monster(health = 20, energy = 50)

print(monster1.health)
print(monster2.health)
