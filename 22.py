# Scope 

multilpier = 10
has_calculated = False

def multiply_calculator(num1):
    result = num1 * multilpier
    global has_calculated
    has_calculated = True
    return result


print(multiply_calculator(5))
print(has_calculated)
