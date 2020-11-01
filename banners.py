# Brittany Brandriff and Wilver Campos
# October 19, 2015
# CS126L Lab 6
# wec24@nau.edu


word = input('Enter a word to print: ')
orientation = input('Enter whether it is vertical (v) or horizontal (h): ')

word.lower()
orientation.lower()

letter_a = [" oo ", "o  o", "oooo", "o  o"]
letter_c = [" oo", "o", "o", " oo"]
letter_t = ["ooooo", "  o", "  o", "  o"]

alphabet = {"a": letter_a, "c": letter_c, "t": letter_t}

def print_banner(word, orientation):
    for letter in word:
        for part in alphabet[letter]:
            if orientation == 'v':
                print(part)

            elif orientation == 'h':
                print(part)

            else:
                print("Error")

print_banner(word, orientation)
