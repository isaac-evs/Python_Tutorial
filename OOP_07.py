# Complex Inheritance

class Monster():

    def __init__(self, health, energy, **kwargs):
        print(kwargs)
        self.health = health
        self.energy = energy
        super().__init__(**kwargs)

    def attack(self, ammount):
        print("The Monster has attacked")
        print(f"It has dealth {ammount} damage")
    
    def move(self, speed):
        print("The Monster has moves")
        print(f"At a speed of {speed} km/h")


class Fish():

    def __init__(self, speed, has_scales, **kwargs):
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(**kwargs)
    
    def swim(self):
        print(f"The fish is swimming at a speed of {self.speed} km/h")


class Shark(Monster, Fish):
    
    def __init__(self, bite_strenght, health, energy, speed, has_scales):
        self.bite_strenght = bite_strenght
        super().__init__(health = health, energy = energy, speed = speed, has_scales = has_scales)


# mro -> method resolution order
# print(Shark.mro())


shark = Shark(
    bite_strenght = 30, 
    health = 50, 
    energy = 40, 
    speed= 120, 
    has_scales = False)