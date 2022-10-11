#!/usr/bin/env python3
# Created by: Kent Gatera
# Created on: Oct 05
# This program checks if a user's integer guess is correct


import random


def main_game():

    max_number = input("What is the highest guessable number?: ")
    # the "isdigit" function checks if the input is a number or not
    # then returns the result as a boolean determining if the statement
    # runs or not.
    if max_number.isdigit():
        print("")
    else:
        print("Please enter a valid input")
    guess_number = input("What is your guess? ")
    random_number = random.randint(1, int(max_number))
    if max_number.isdigit():
        print("")
    else:
        print("Please enter a valid input")
    # checks if your guess is a number.
    if guess_number.isdigit():
        if guess_number == random_number:
            print("Your're correct!")
        else:
            print("Wrong, try again.")
            print("The number was:")
            print(random_number)
    else:
        print("Please enter a valid input")


if __name__ == "__main__":
    main_game()
