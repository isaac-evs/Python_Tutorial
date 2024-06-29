# Functions

def calculator(num1, num2, operation):
    match operation:
        case "adission": 
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        case "substraction": 
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        case "multiplication": 
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        case "division": 
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")



calculator(5, 3, "division")