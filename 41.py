# Decorators inside classes
from datetime import datetime

class Generic:

    def __init__(self):
        self._x = 10

    def getter(self):
        print(datetime.now())
        return self._x

    def setter(self,value):
        print("set x")
        self._x = value

    def deleter(self):
        print("delete x")
        del self._x

    x = property(getter, setter, deleter)

generic = Generic()
generic.x = 4
print(generic.x)
del generic.x

###################################

class Generic2:

    def __init__(self):
        self._y = 5

    @property
    def y(self):
        print("getting y")
        return self._y

    @y.setter
    def y(self, value):
        print("setting y")
        self._y = value

    @y.deleter
    def y(self):
        print("deleting y")
        del self._y

generic2 = Generic2()
generic2.y
generic2.y = 8
print(generic2.y)
del generic2.y
