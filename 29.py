# Map / Filter

# map
my_list = [1,2,3,4,5]

print(list(map(lambda num: num ** 2, my_list)))


# filter
print(list(filter(lambda num: num < 4, my_list)))
print("\n")

###################################################

list_comp = [num ** 2 for num in my_list if num < 4]

print(list_comp)