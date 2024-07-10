#Function basics

def my_function():
    print("Hello World!")

def my_wrapper(my_function):
    print(" ######### ")
    my_function()
    print(" ######### ")

def function_generator():
    def new_function():
        print("new function")
    return new_function

new_func = function_generator()
new_func()
