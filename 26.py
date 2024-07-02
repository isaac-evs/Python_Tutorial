#List Comprehension

#my_list=[(num, num) if num <= 10 else 0 for num in range(0,100)]

#print(my_list)

inventory_names = ['Screws', 'Wheels', 'Metal parts', 'Rubber bits', 'Screwdrivers', 'Wood']
inventory_numbers = [43, 12, 95, 421, 23, 43]

replenish_list = [(name, number) for name, number in zip(inventory_names, inventory_numbers) if number < 25]

print(replenish_list)
print("\n")

#Combine list comprehension

combined_comp = [[(i, j) for i in range(5)] for j in range(10)]

for i in combined_comp:
    print(i)
print("\n")

#Chess board

chess_board = [[(letter, num + 1) for letter in ("a","b","c","d","f","g","h")[::-1]] for num in range(8)]

for i in chess_board:
    print(i)