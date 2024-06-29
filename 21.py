# Parameters II 

# List unpacking
def print_all(*arguments):
    print(arguments)
    for i in arguments:
        print(i)

#print_all(1,2,3,4,5,6,"Hello",8,9)


# Keyword unpacking 
def print_more(**arguments):
    print(arguments)


#print_more(arg1 = "1", arg2 = "test", arg3 = [1,2,3])


# Combinging both 

def print_even_more(*args, **kwargs):
    print(args)
    print(kwargs)


#print_even_more(1,2,4,5, arg6 = "hello", arg7 = "world")


########################################################


def calculator(*nums):
    result = sum(nums)
    print(result)

    

calculator(1,5,8,12,3,4,8,9)