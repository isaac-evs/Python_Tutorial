# Decorators

import time

#traditional

def decoractor(my_function):
    def wrapper():
        print(" ######## ")
        my_function()
        print(" ######## ")
    return wrapper

def my_function():
    print("function")

my_function = decoractor(my_function)
my_function()

################################

#decorator
def decorator2(my_function2):
    def wrapper():
        print(" ####### ")
        my_function2()
        print(" ###### ")
    return wrapper

@decorator2
def my_function2():
    print("function 2")

my_function2()

#############################

#timer

def timer_decorator(my_function3):
    def wrapper():
        start_time = time.time()
        my_function3()
        duration = time.time() - start_time
        print(f"duration: {duration}")
    return wrapper

def twice_decorator(my_function3):
    def wrapper():
        my_function3()
        my_function3()
    return wrapper

@twice_decorator
@decoractor
@timer_decorator
def my_function3():
    print("function 3")
    time.sleep(1)

my_function3()
