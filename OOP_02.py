# Dunder methods

class Monster:

    #attributes
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    #Other dunder methods

    def __len__(self):
        return self.health

    def __abs__(self):
        return self.energy
    
    def __call__(self):
        return "The monster was called"
    
    def __add__(self, other):
        return self.health + other
    
    def __str__(self):
        return f"A monster with health = {self.health}, and energy = {self.energy}"
    
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
print(len(monster1))
print(abs(monster1))

print(monster1.__dict__)
print(vars(monster1))

print(monster1())

print(monster1 + 10)

print(monster1)