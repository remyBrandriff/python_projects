# Remy Brandriff
# CS499 - Bioinformatics
# Assignment 3
# A prefix trie performing the k-mer functionality from HW 1
# 03/30/19
import time
from typing import Tuple


# Create a trie node
class Node(object):

    # Initialize node
    #   Char = character in the node
    #   Children = list of children in the node; each node will have the four nucleobases (A, C, G, T)
    #   End = is this the last character in the word?
    #   Count = how many times do we find this?
    def __init__(self, char: str):
        self.char = char
        self.children = []
        self.end = False
        self.count = 1


# Add word to the prefix trie
def add_to_trie(root, word: str):

    # Set the node as the root
    node = root

    # Check if the word is already there
    for i in word:
        in_child = False

        # Is the character in the node's children?
        for child in node.children:

            # If yes, add it to the count and go down this path
            if child.char == i:
                child.count += 1
                node = child
                in_child = True
                break

        # If not, add it in
        if not in_child:
            new = Node(i)
            node.children.append(new)
            node = new

    # Return that we've reached the end of the word and each character has been added to the trie
    node.end = True


# Find the prefix in the tree, and return a Tuple with yes it appears/no it doesn't, and if so, how many times
def find_in_trie(root, prefix: str) -> Tuple[bool, int]:
    node = root

    # If the trie is empty, just end right here, obviously the prefix won't be in it
    if not root.children:
        return False, 0

    # Now if we have a trie, check if the prefix exists in the trie
    for i in prefix:
        found = False

        for child in node.children:
            if child.char == i:
                found = True
                node = child
                break

        # If the prefix isn't there, return false
        if not found:
            return False, 0

    return True, node.count


# Run the program
if __name__ == '__main__':

    # Open the file and read in the genome
    file_name = "NC003997_sequence.fasta"

    with open(file_name) as file:
        lines = file.read().splitlines()

    # Get the sequence (everything but the header)
    sequence = ""
    sequence = sequence.join(lines[1:])

    # Create the root node, which will just be ' ', which creates the trie
    root = Node(' ')

    start = time.time()
    # Add words to the trie
    for i in range(len(sequence)):
        mer = sequence[i:i+4]
        add_to_trie(root, mer)

    # Check if a word is in the trie and print the results
    mer_file = "4mers.txt"
    with open(mer_file) as file2:
        for i in file2:
            mer = i.strip()
            print(mer + " " + str(find_in_trie(root, mer)) + ", " + str(time.time()))

    end = time.time()
    fourmer_time_passed = end - start

    print("4-mers: " + str(fourmer_time_passed))
