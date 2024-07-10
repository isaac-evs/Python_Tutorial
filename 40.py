# Decorators paramaters

def repetition_decorator(repetitions):
    def decorator(my_function):
        def wrapper():
            for num in range(repetitions):
                my_function()
        return wrapper
    return decorator

@repetition_decorator(5)
def my_function():
    print("Hello World!")

my_function()
