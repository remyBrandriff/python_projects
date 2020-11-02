'''
def is_there_a_vowel(x):
    while x == "N":
        word = input("Enter a word: ")
        word.lower()
        if ("a" in word) or ("e" in word) or ("i" in word) or ("u" in word) or ("y" in word):
            print("True")
            x = input("Are you finished? Y/N ")
            x.upper()
        else:
            print("False")
            x = input("Are you finished? Y/N ")
            x.upper()
        
x = "N"
is_there_a_vowel(x)

'''

def word_score(word, letter_values):
    word.lower()
    i = len(word)
    for x in range(i):
        if letter_values.keys() in word:
            print(


#word = input("Enter a word to test for scrabble score: ")

letter_values = { "a": 1, "b": 3, "c": 3,
                  "d": 2, "e": 1, "f": 4,
                  "g": 2, "h": 4, "i": 1,
                  "j": 8, "k": 5, "l": 1,
                  "m": 3, "n": 1, "o": 1,
                  "p": 3, "q": 10, "r": 1,
                  "s": 1, "t": 1, "u": 1,
                  "v": 4, "w": 4, "x": 8,
                  "y": 4, "z": 10 }

print(word_score("Hello", letter_values))
#print(word_score("Equation", letter_values))
#print(word_score("Zebra", letter_values))
#print(word_score("Test", letter_values))
#print(word_score("Zilch", letter_values))
