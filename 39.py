# Decorator arguments

def decorator(my_function):
    def wrapper(*args, **kwargs):
        print("#####")
        my_function(*args, **kwargs)
        print("#####")
    return wrapper

@decorator
def my_function(function_parameter):
    print(function_parameter)

my_function("Hello World!")
