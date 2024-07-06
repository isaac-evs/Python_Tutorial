# Classes 

class Monster:

    #attributes
    health = 90
    energy = 40

    #methods
    def attack(self, amount):
        print("The monster has attacked")
        print(f"{amount} demage was dealt")
        monster.energy -=10
        print(monster.energy)
    
    def move(self, speed):
        print("The monster has moved")
        print(f"moving at {speed} km/h")


monster = Monster()
monster.move(20)
