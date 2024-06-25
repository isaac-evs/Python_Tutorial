# While loop
x = 0

while x < 10:

    x += 1

    if x == 5:
        continue

    print(x)
   

##################

y = 0

my_list = []

while y < 100:

    y += 1

    if y == 58:
        continue

    if y % 2 == 0:
        my_list.append(y)

print(my_list)