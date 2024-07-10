# Exceptions / Error Handling

# Anticipating errors
try:
    print("try")
    print(1/0)
except ZeroDivisionError:
    print("You cant divide by 0")
except NameError:
    print("Does not exist")
else:
    print("else")
finally:
    print("finally...")

###########################

# Raising exceptions
must_be_string = "Hello"
if isinstance(must_be_string, str):
    print(must_be_string)
else:
    raise TypeError("Must be a string")

############################

# Assert
a = 5
assert a == 5

###########################

# Exercise

my_list = [1,2,3,4]
index = 5

try:
    my_list[2]
except IndexError:
    print("Index doesnt exist")
else:
    print("The index exists")
finally:
    print("Process end")

if len(my_list) > index :
    print(my_list[index])
else:
    raise IndexError("Index out of range")
