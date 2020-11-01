# Authors: Brittany Brandriff and Jon Derr
# Date: 5 October 2015
# Description: This program functions as a basic grade calculator
#              to determine a grade using a weighted average

# Scores
hw1 = [39, 40, 29, 40, 0, 5]
hw2 = [40, 40, 40, 40, 40, 5]
quiz1 = [10, 10, 9, 2, 10, 10, 10]
quiz2 = [10, 10, 10, 10, 10, 10, 10]
test1 = [293, 284, 300]
test2 = [300, 300, 300]

# Weights
hw_w = .2
quiz_w = .2
test_w = .6

# Calculate percentages


def percentage_homework(hw1, hw2):
    hw_per = (((sum(hw1)/sum(hw2)) * 100) // 1)
    return hw_per


def percentage_quizzes(quiz1, quiz2):
    quiz_per = (((sum(quiz1)/sum(quiz2)) * 100) // 1)
    return quiz_per


def percentage_tests(test1, test2):
    test_per = (((sum(test1)/sum(test2)) * 100) // 1)
    return test_per

# Calculate letter grades


def lettergrade_hw(per_hw):
    if per_hw >= 90.0:
        lettergrade = "A"
    elif per_hw >= 80.0:
        lettergrade = "B"
    elif per_hw >= 70.0:
        lettergrade = "C"
    elif per_hw >= 60.0:
        lettergrade = "D"
    else:
        lettergrade = "F"
    return lettergrade


def lettergrade_quiz(per_quiz):
    if per_quiz >= 90.0:
        lettergrade = "A"
    elif per_quiz >= 80.0:
        lettergrade = "B"
    elif per_quiz >= 70.0:
        lettergrade = "C"
    elif per_quiz >= 60.0:
        lettergrade = "D"
    else:
        lettergrade = "F"
    return lettergrade


def lettergrade_test(per_test):
    if per_test >= 90.0:
        lettergrade = "A"
    elif per_test >= 80.0:
        lettergrade = "B"
    elif per_test >= 70.0:
        lettergrade = "C"
    elif per_test >= 60.0:
        lettergrade = "D"
    else:
        lettergrade = "F"
    return lettergrade

# Calculate final letter grade


def lettergrade_final(final_score):
    if final_score >= 90.0:
        lettergrade = "A"
    elif final_score >= 80.0:
        lettergrade = "B"
    elif final_score >= 70.0:
        lettergrade = "C"
    elif final_score >= 60.0:
        lettergrade = "D"
    else:
        lettergrade = "F"
    return lettergrade

# Calculate weighted scores


def weighted_hw_score(per_hw, hw_w):
    hw_weighted = per_hw * hw_w
    return hw_weighted


def weighted_quiz_score(per_quiz, q_w):
    quiz_weighted = per_quiz * q_w
    return quiz_weighted


def weighted_test_score(per_test, t_w):
    test_weighted = per_test * t_w
    return test_weighted

# Function calls

per_hw = (percentage_homework(hw1, hw2))
per_quiz = (percentage_quizzes(quiz1, quiz2))
per_test = (percentage_tests(test1, test2))
hw_lettergrade = (lettergrade_hw(per_hw))
quiz_lettergrade = (lettergrade_quiz(per_quiz))
test_lettergrade = (lettergrade_test(per_test))
hw_weight = (weighted_hw_score(per_hw, hw_w))
quiz_weight = (weighted_quiz_score(per_quiz, quiz_w))
test_weight = (weighted_test_score(per_test, test_w))

final_score = hw_weight + quiz_weight + test_weight
final_lettergrade = (lettergrade_final(final_score))

# Output

print("Homework Grade: %d, (%s)" % (per_hw, hw_lettergrade))
print("Quiz Grade: %d, (%s)" % (per_quiz, quiz_lettergrade))
print("Test Grade: %d, (%s)" % (per_test, test_lettergrade))
print("Final Score: %d, (%s)" % (final_score, final_lettergrade))
