# For loops

my_list = [[10,40,20,50], [2,42,10], [101,12,4]]

for i in my_list:
    for j in i:
        if j < 50:
            if j < 10:
                continue
            print(j)
        if j > 100:
            break