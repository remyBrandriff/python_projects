# Authors: Brittany Brandriff, Nick Bollone
# Date: 28 September 2015
# Description: A math quiz with three levels
# (Beginner, Intermediate, andAdvanced)

from random import randint

# User chooses number of questions and level
numQuestion = int(input("Enter the number of questions in the quiz: "))
level = input("Enter the quiz level (Beginner, Intermediate, Advanced): ")
correct = 0

level = level.lower()  # auto-corrects all user input into lowercase letters

if level == "beginner":
    for i in range(numQuestion):
        n1 = randint(1, 10)  # choose random number from 1 to 10
        n2 = randint(1, 10)

        add = n1 + n2  # if addition
        sub = n1 - n2  # if subtraction

        prob = randint(1, 2)
        if prob == 1:
            # Addition question
            ans = int(input("What is %d + %d? " % (n1, n2)))
            if ans == add:
                print("That's correct! \n")
                correct = correct + 1
            else:
                print("That is not correct. The actual answer is %d. \n" % add)

        if prob == 2:
            # Subtraction question
            ans = int(input("What is %d - %d? " % (n1, n2)))
            if ans == sub:
                print("That's correct! \n")
                correct = correct + 1
            else:
                print("That is not correct. The actual answer is %d. \n" % sub)

        result = correct/numQuestion  # calculates percentage of right answers

        if result >= 2/3:
            print("You got all of them right!")

        elif result >= 1/3:
            print("You need more practice.")

        else:
            print("Please ask your math teacher for help.")

elif level == "intermediate":
    for i in range(numQuestion):
        n1 = randint(1, 25)
        n2 = randint(1, 25)

        add = n1 + n2
        sub = n1 - n2
        div = n1 / n2
        mul = n1 * n2

        prob = randint(1, 4)
        if prob == 1:
            # Addition
            ans = int(input("What is %d + %d? " % (n1, n2)))
            if ans == add:
                print("That's correct! \n")
                correct = correct + 1
            else:
                print("That is not correct. The actual answer is %d. \n" % add)

        elif prob == 2:
            # Subtraction
            ans = int(input("What is %d - %d? " % (n1, n2)))
            if ans == sub:
                print("That's correct! \n")
                correct = correct + 1
            else:
                print("That is not correct. The actual answer is %d. \n" % sub)

        elif prob == 3:
            # Division
            ans = float(input("What is %d / %d? " % (n1, n2)))
            if ans == div:
                print("That's correct! \n")
                correct = correct + 1
            else:
                print("That is not correct. The actual answer is %d. \n" % div)

        elif prob == 4:
            # Multiplication
            ans = int(input("What is %d * %d? " % (n1, n2)))
            if ans == mul:
                print("That's correct! \n")
                correct = correct + 1
            else:
                print("That is not correct. The actual answer is %d. \n" % mul)

        # Calculates percentage of correct answers
        result = correct/numQuestion

        if result >= 2/3:
            print("You got all of them right!")

        elif result >= 1/3:
            print("You need more practice.")

        else:
            print("Please ask your math teacher for help.")

elif level == "advanced":
    # Custom questions hard-coded in
    for i in range(numQuestion):
        # Random numbers from 1 to 50
        n1 = randint(1, 50)
        n2 = randint(1, 50)
        n3 = randint(1, 50)

        prob = randint(1, 5)

        if prob == 1:
            ans = float(input('What is %d + %d * %d? \n' % (n1, n2, n3)))
            a = n1 + n2 * n3
            if ans == a:
                print('Correct')
                correct = correct + 1
            else:
                print('Not correct')

        elif prob == 2:
            ans = float(input('What is %d / %d * %d \n' % (n1, n2, n3)))
            a = n1 / n2 * n3
            if ans == a:
                print('Correct')
                correct = correct + 1
            else:
                print('Not correct')

        elif prob == 3:
            ans = float(input('What is %d - %d * %d \n' % (n1, n2, n3)))
            a = n1 - n2 * n3
            if ans == a:
                print('Correct')
                correct = correct + 1
            else:
                print('Not correct')

        elif prob == 4:
            ans = float(input('What is %d * %d - %d \n' % (n1, n2, n3)))
            a = n1 * n2 - n3
            if ans == a:
                print('Correct')
                correct = correct + 1
            else:
                print('Not correct')

        elif prob == 5:
            ans = float(input('What is %d / %d + %d \n' % (n1, n2, n3)))
            a = n1 / n2 + n3
            if ans == a:
                print('Correct')
                correct = correct + 1
            else:
                print('Not correct')

        # Calculates percentage of correct answers
        result = correct/numQuestion

        if result >= 2/3:
            print("You got all of them right!")

        elif result >= 1/3:
            print("You need more practice.")

        else:
            print("Please ask your math teacher for help.")

# In case the user enters incorrect input
else:
    print("Input not recognized")
