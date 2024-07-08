# Class and Methods 

class Monster:

    def __init__(self, func):
         self.attack = func


class Attacks:
     
    def bite(self):
        print("Monster bites")

    def strike(self):
        print("Monster strikes")
    
    def slash(self):
        print("Monster slashes")
    
    def kick(self):
        print("Monster kicks")


monster = Monster(func = Attacks().bite)
monster.attack()