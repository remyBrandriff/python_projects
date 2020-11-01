# Author: Brittany Brandriff
# CS126L Lab 7
# November 1, 2015
# A short trivia game with superhero/comic book questions
from random import shuffle

# question list with answers
questions_list = [
    {"question": "What DC villain is Mark Hamill most famous for playing?",
     "answers": [
         "The Trickster", "The Joker",
         "Sinestro", "Lex Luthor"],
     "correct": 2},
    # Hamill DID play the Trickster
    # but voicing the Joker is his most famous role

    {"question": "Which of the following characters is \n"
     "NOT blood-related to Wolverine?",
     "answers": [
         "Laura Kinney", "Daken", "Sabretooth",
         "Avery Connor", "Erista"],
     "correct": 3},
    # Sabretooth is the only option who is not either Wolverine's clone
    # Or his child
    # Also not his brother, despite the midleading Origins movie

    {"question": "Who was the first Robin?",
     "answers": [
         "Jason Todd", "Tim Drake", "Barbara Gordon",
         "Dick Grayson", "Damian Wayne"],
     "correct": 4},
    # All but Barbara have been Robin, but Dick was the first

    {"question": "Who has NOT been active as a \n"
     "speedster superhero in the DC comics?",
     "answers": [
         "Barry Allen", "Wally West", "Iris West",
         "Jay Garrick", "Bart Allen", "Jai West",
         "Max Mercury", "Jesse Chambers", "Harrison Wells"],
     "correct": 9},
    # Harrison Wells was a speedster in the show, but not in the comics

    {"question": "Who has not led the X-Men?",
     "answers": [
         "Wolverine", "Charles Xavier",
         "Quentin Quire", "Magneto", "Emma Frost"],
     "correct": 3},
    # Quentin is a little shit. That is all.

    {"question": "What is the Scarlet Witch's mutant power?",
     "answers": [
         "Telekinesis", "Reality Warping",
         "Chaos Manipulation", "Magic"],
     "correct": 3},
    # She manifests all of these abilities as an extension
    # of her innate ability to manipulate chaos

    {"question": "Who has not been Batman?",
     "answers": [
         "Dick Grayson", "Bruce Wayne", "Thomas Wayne",
         "Commissioner Jim Gordon", "Terry McGinnis",
         "Jason Todd", "Ra's al Ghul"],
     "correct": 7},
    # Ra's is the only person who hasn't been Batman
    # in some form or alternate universe

    {"question": "Who was not one of the original Teen Titans?",
     "answers": [
         "Raven", "Aqualad", "Kid Flash", "Robin",
         "Speedy", "Wonder Girl"],
     "correct": 1},
    # Raven was not one of the original Titans line-up in the comics
    # just in the cartoon and in later teams

    {"question": "In the TV show, Agents of S.H.I.E.L.D.,"
     "which of Coulson's original team originated in the comics?",
     "answers": [
         "Phil Coulson", "Melinda May", "Mary-Sue 'Skye' Poots",
         "Leopold Fitz", "Jemma Simmons", "Grant Ward"],
     "correct": 3},
    # Skye's comic book equivalent is Daisy "Quake" Johnson,
    # one of Fury's Secret Warriors/Secret Avengers,
    # and former Director of SHIELD

    {"question": "Where did the Marvel character X-23/Laura Kinney/Wolverine \n"
     "originate?",
     "answers": [
         "X-Men: Evolution", "Uncanny X-Men comic series",
         "X-23 solo series", "Weapon-X comic series"],
     "correct": 1},
    # X-23 was originally created for the cartoon,
    # and was later adapted to the comics
    ]

options = [
    {"option": [
        "Play the game", "View game credits", "Quit"]}
]

# Title and intro statement
print("Welcome to the CS126 Trivia Game, Comic Book Edition!")
print("Can you correctly answer these (relatively) \n"
      "easy trivia questions about our favorite superheroes and villains?")
print("= = = = = = = = = = = = = = = = = = =")
print("WIN MILLIONS!! Well, probably not, but WIN BRAGGING RIGHTS! \n"
      "(also unlikely).")
print("Maybe you'll win a batarang cookie or something. That's doable. \n"
      "Give us a break, we're on a budget.")
print("= = = = = = = = = = = = = = = = = = =")

# Main menu
print("Main Menu")
print("= = = = = = = = = = = = = = = = = = =")
print("Please select one of the following options.")

# Prints menu choices from Options list, asks for user input
for question_dict in options:
    for i, choice in enumerate(question_dict["option"]):
        print(str(i + 1) + ". " + choice)
menu_choice = input("Enter the number of your choice: ")
print("= = = = = = = = = = = = = = = = = = =")

if menu_choice == 1:

    # sets score counter to zero
    score = 0

    # shuffles the questions so they're given in random order
    shuffle(questions_list)

    # gives the questions and answer options to user, requests an answer,
    # evaluates and prints if write or wrong
    for question_dict in questions_list:
        print(question_dict["question"])
        for i, choice in enumerate(question_dict["answers"]):
            print(str(i + 1) + ". " + choice)
        answer = input("Choose an answer (ex: 1): ")
        if answer == question_dict["correct"]:
            print("Good job. "
                  "Imagine non-ironic confetti falling around you.")
            score += 1
            print("Your current score is"), score
            print("= = = = = = = = = = = = = = = = = = =")
        else:
            print("Incorrect. The confetti machine is broken, though, \n"
                  "so just pretend it's an ironic show of your failure.")
            score += 0
            print("Your current score is"), score
            print("= = = = = = = = = = = = = = = = = = =")

    # Prints final score and an appropriate, if snarky, message
    print("Your final score is"), score
    if score == 10:
        print("You're a pro!")
        print("Well, not really, because these questions were fairly easy, \n"
              "but still impressive.")
    elif score >= 9:
        print("Pretty good. You only missed one.")
    elif score >= 6:
        print("Not bad. You're certainly not an avid superhero fan, \n"
              "but you know common knowledge.")
    elif score == 5:
        print("Maybe you should start reading more comics and \n"
              "paying more attention at the movies...")
    elif score <= 4:
        print("Please direct yourself to the nearest comic book shop \n"
              "and tell them you are in dire need of help.")


if menu_choice == 2:
    # Prints credits
    print("This game was created by Remy Brandriff for CS126L, 2017")

if menu_choice == 3:
    # Exits game
    exit()
