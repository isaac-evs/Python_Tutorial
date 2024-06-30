# Documenting Functions 

def function(a:int = 10, b:int = 10):
    """A simple function that prints 2 parameters"""
    result = a + b
    print(result)

function(5,10)
print(function.__doc__)