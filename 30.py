# List Comprehension excercises (Extra)

# 1 Find all the numbers from 1 - 1000 that are divisible by 7

my_list1 = [num for num in range(1000) if num % 7 == 0]

# 2 Find all the numbers from 1 - 1000 that have 3 in them

my_list2 = [num for num in range(1000) if "3" in str(num)]

# 3 Count the number of spaces in a string

fruits = ["apple", "ban  an a", "waterme lon"]

my_list3 = [item.count(" ") for item in fruits]

# 4 Creata a list with all the consonants in the string

my_string = "Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"

my_list4 = [letter for letter in my_string if letter not in "a,e,i,o,u,' '"]

print(my_list4)
