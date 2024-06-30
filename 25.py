# Better for loops

inventory_names = ['Screws', 'Wheels', 'Metal parts', 'Rubber bits', 'Screwdrivers', 'Wood' ]
inventory_numbers = [43, 12, 95, 421, 23, 43]

#Zip
#for item, id in zip(inventory_names, inventory_numbers):
#   print(f"{item} current inventory id: {id}")

#Enamurate
#for index, item in enumerate(inventory_names):
#   print(f"{index}: {item}")


#########################################################


for item in enumerate(zip(inventory_names, inventory_numbers)):
    print(f"{item[1][0]} [id: {item[0]}] - inventory: {item[1][1]}")