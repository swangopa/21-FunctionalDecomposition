"""
Hangman.

Authors: Paige Swango and Miguel Cooper.
"""  # DONE: 1. .

# TODO: 2. Implement Hangman using your Iterative Enhancement Plan.

####### Do NOT attempt this assignment before class! #######
import random
def main():
    length = length_word()
    while True:
        word = random_word()
        if length <= len(word):
            break
    print(word)
    over = input("How manyy unsuccessful choices do you want to allow yourself?")
    guess = input("What letter do you want to try?")
    print(guess)




def random_word():
    with open('words.txt') as f:
        f.readline()
        string = f.read()
        words = string.split()

        r = random.randrange(0,len(words))
        word = words[r]
        print(word)
        return word

def length_word():
    number = input("what minimum length do you want for the secret word?")
    number = int(number)
    return number



main()
