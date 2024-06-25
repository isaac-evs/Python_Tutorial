# Match Case

grade = 2

match grade:
    case 1:
        print("Very good")
    case 2:
        print("Good")
    case 3:
        print("Average")
    case 4:
        print("Bad")
    case 5:
        print("Very bad")
    case _:
        print("range must be 1 - 5")