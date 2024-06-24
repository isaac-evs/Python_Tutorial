my_list = [1,2,3,4]

my_string = str(my_list).strip("[").strip("]").replace(",","")

print(my_string)