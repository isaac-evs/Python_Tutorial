# Scope and Classes

def update_health(amount):
    monster.health += amount

class Monster:

    def __init__(self, health, energy):
        self.health = health
        self.set_energy(energy)
    
    def update_energy(self, ammount):
        self.energy += ammount

    def set_energy(self, energy):
        new_energy = energy * 2
        self.energy = new_energy

monster = Monster(health = 100, energy = 100)

update_health(20)

print(monster.health)

monster.update_energy(50)

print(monster.energy)