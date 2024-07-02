# Other Comprehension

# Set
set_comp = {num for num in range(100)}
print(set_comp)
print("\n")

# Dictionary
dictionary_comp = {num: num ** 2 for num in range(100)}
print(dictionary_comp)
print("\n")

#tuple
tuple_comp = tuple(num for num in range(100))
print(tuple_comp)
print("\n")

###############################################

my_dictionary = {key: [1,2,3,4,5] for key in "ABCDE"}

print(my_dictionary)