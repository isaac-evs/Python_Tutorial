# File handling

# read
with open("test.txt","r") as file:
    print(file.read())

# write 
with open("test.txt", "a") as file:
  file.write("\nWrite some more text")

# create 
with open("new.txt", "w") as file:
  file.write("This is a new txt file")


##########################################


with open("tree.txt", "w") as file:
    file.write("   #  \n   ##  \n  ####  \n   ll  ")