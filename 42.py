# Decorators in classes excercise
class Character:

    def __init__(self, name, health, mana, level):
        self.name = name
        self.health = health
        self.mana = mana
        self.level = level

    #Name
    #############################
    @property
    def name(self):
        print("getting name")
        return self._name

    @name.setter
    def name(self, value):
        if value.isalpha() == True:
            print("setting name")
            self._name = value
        else:
            print("cant set name")

    @name.deleter
    def name(self):
        print("deleting name")
        self._name = None

    #Health
    #############################
    @property
    def health(self):
        print("getting health")
        return self._health

    @health.setter
    def health(self, value):
        if value >= 0:
            print("setting health")
            self._health = value
        else:
            print("cant set health")

    @health.deleter
    def health(self):
        print("deleting health")
        self._health = None

    #Mana
    #############################
    @property
    def mana(self):
        print("getting mana")
        return self._mana

    @mana.setter
    def mana(self, value):
        if value >= 0:
            print("setting mana")
            self._mana = value
        else:
            print("cant set mana")

    @mana.deleter
    def mana(self):
        print("deleting mana")
        self._mana = None

    #Level
    #############################
    @property
    def level(self):
        print("getting level")
        return self._level

    @level.setter
    def level(self, value):
        if value >= 0:
            print("setting level")
            self._level = value
        else:
            print("cant set level")

    @level.deleter
    def level(self):
        print("deleting level")
        self._level = None

#Default values
character = Character(name = "Player", health = 100, mana = 20, level = 1)

#Set
character.name = "Tom"
character.health = 120
character.mana = 40
character.level = 5

#Get
print(character.name)
print(character.health)
print(character.mana)
print(character.level)

#Invalid values
try:
    character.name = "Arthur 123"
except ValueError:
    print(ValueError)

try:
    character.health = -20
except ValueError:
    print(ValueError)

#Delete
del character.level
print(character.level)
