# Scope and Classes (Excercise)

class Monster:

    def __init__(self, health, energy):
        self.health = health
        self.energy = energy
    
    def get_damage(self, ammount):
        monster.health -= ammount

class Hero:

    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster

    def attack(self, ammount):
        monster.get_damage(ammount)


monster = Monster(health = 100, energy = 50)


hero = Hero(damage = 20, monster = monster)


print(monster.health)


hero.attack(hero.damage)


print(monster.health)