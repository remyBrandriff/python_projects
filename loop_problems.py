terminate = "N"
food = []

while (terminate == "N"):
    name = input("Enter name: ")
    print("Enter your three favorite foods")
    food[0] = input("1. ")
    food[1] = input("2. ")
    food[2] = input("3. ")
    fave_foods = {name: food}
    
    terminate = input("Are you finished entering data? Y/N ")
    terminate.upper()
    

print(fave_foods)
