# Brittany Brandriff, Michael Johnson
print("Good morning! You're alarm goes off at 8 AM, and you have a class at "
      "9:30 AM.")
print(" ")
# Choice 1
choice1 = input("Do you hit SNOOZE or GET UP? ")

if choice1 == "SNOOZE":
                print("You get to sleep in a little later, but oversleep "
                      "but you wake up at 9:20! You  "
                      "have a class in 10 minutes.")
                print(" ")
                # choice 2
                choice2 = input("Do you try to RUN it or take the BUS? ")
                if choice2 == "RUN":
                    print("Congrats! You just barely made it, "
                          "and it turns out you have a test "
                          "today. You  ace it.")
                elif choice2 == "BUS":
                    print("Sorry! There was an accident on "
                          "the road and you're stuck there "
                          "for awhile.")
                # Choice 2 ERROR
                else:
                    print("You screwed up and entered the wrong answer. "
                          "You fail at life.")
                    # Choice 3
                    choice3 == input("Do you wait and go to "
                                     "CLASS late, or go "
                                     "HOME? ")
                    if choice3 == "CLASS":
                        print("You try to sneak in, but "
                              "the professor catches "
                              "you and kicks you out. "
                              "You fail the test.")
                    elif choice3 == "HOME":
                        print("As it turns out, you "
                              "missed a major test, "
                              "and failed the class.")
                    # Choice 3 Error
                    else:
                        print("You screwed up and entered the wrong answer."
                              "You fail at life.")
elif choice1 == "GET UP":
    # Choice 4
    choice4 = input("Do you take a SHOWER, do HOMEWORK, or get BREAKFAST? ")
    if choice4 == "SHOWER":
        print("You feel refreshed, go to class on time and ace "
              "the test")
    elif choice4 == "HOMEWORK":
        print("You get to class on time, but you're burnt out "
              "from the homework and fail the test.")
    elif choice4 == "BREAKFAST":
        print("You arrive at the dining hall.")
        # Choice 5
        choice5 = input("How many servings do you have?")
        choice5 = int(choice5)

        if choice5 > 2:
            print("You feel refreshed, go to class on time, "
                  "and ace the test.")
        else:
            print("You over-ate, got sick, and had to "
                  "go to the hospital. You missed the test "
                  "and failed.")
# Choice 1 ERROR
else:
    print("You screwed up and entered the wrong answer. You fail at life.")
