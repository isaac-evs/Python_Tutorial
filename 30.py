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

# 5 Get the index and the value as a tuple for items in the list

item_list = ["hi", 4, 8.99, "apple", ("t","b","n")]

my_list5 = {(index, item) for index, item in enumerate(item_list)}

# 6 Find the common numbers in two lists (without using a tuple or set)

list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

my_list6 = [num for num in list_a if num in list_b]

# 7 Get only the numbers in a sentence

sentence = 'In 1984 there were 13 instances of a protest with over 1000 people attending'

my_list7 = [letter for letter in sentence if letter.isnumeric()]

# 8 Given numbers = range(20), produce a list containing the word 'even' if a number in the numbers is even, and the word 'odd' if the number is odd.

my_list8 = ["even" if num % 2 == 0 else "odd" for num in range(20)]

# 9 Produce a list of tuples consisting of only the matching numbers in these lists

list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_b = [2, 7, 1, 12]

my_list9 = [(num1, num2) for num1 in list_a for num2 in list_b if num1 == num2]

print(my_list9)
