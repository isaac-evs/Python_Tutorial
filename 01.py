# How code is executed

r = int(input("Enter a height for your tree:"))

#Leafs
for i in range(r):
    x = r - (i + 1) // 2
    print(" " * x, end='')
    for j in range(1+i):
        print("#", end='')
    print()

#Trunk
print(" " * (r-1) + "||")