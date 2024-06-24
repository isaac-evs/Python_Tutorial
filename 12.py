my_set = {1,2,3,4,4}

my_list = list(my_set)

print(my_list[0])

##################

set1 = {1,2,3,4}
set2 = {4,5,6,7}

print(set1.union(set2))
print(set1 | set2)

print(set1.intersection(set2))
print(set1 & set2)

print(set1.difference(set2))
print(set1 - set2)

##################

list = (43,25,324,234,5,2,32423,524,534,324,23,54,65,323,42,4,123,123,5,1,321,3124,123,123,124,1,31,22,145)
set = set(list)

print(len(list) == len(set))