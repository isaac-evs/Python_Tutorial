# Sorting Data 

my_list = [('A', 6), ('B', 2), ('C',8), ('D',1)]

print(sorted(my_list, key = lambda item: item[1]))  
print("\n")

###############################################


inventory_names = ['Screws', 'Wheels', 'Metal parts', 'Rubber bits', 'Screwdrivers', 'Wood' ]
inventory_numbers = [43, 12, 95, 421, 23, 43]

combined_list = list(zip(inventory_names,inventory_numbers))

print(sorted(combined_list, key = lambda item: item[1]))

def my_func(item):
    item = len(item[0])
    return item

sorted_list = (sorted(combined_list, key = my_func))

print(sorted_list)

print(len(combined_list[0][0]))