'''
number guessing game

have to keep guessing until you get them all
the game will keep telling whether to go higher or lower to get the closest number you havent guessed yet, biasing towards lower

the numbers are distinct
you can quit the game any-time by typing 'q'

If a lower number is guessed, you must print:
    'The closest to [guess] is lower'
elif a higher number is guessed, you must print:
    'The closest to [guess] is higher'
elif a number in the list is guessed, you must print:
    'You found [guess]! It was in the list'

If the player wins, you must print:
    'Congratulations! You won!'

These outputs are important because of the testing
'''

import random
import math

MIN = 0
MAX = 10
NUM_VALUES = 3


def handle_guess(guess, values):
    duplicate = list(values)
    found = False
    for x in duplicate:
        if guess == x:
            duplicate.remove(guess)
            found = True
            print("You found %d! It was in the list" % (guess))
            break
    if found == False:
        closest = find_closest(guess)
        if guess < closest: 
            print("the closest to %d is higher" % (guess))
        else:
            print("the closest to %d is lower" % (guess))

    return duplicate


        

    # complete your solution here
    # This function should return a duplicate list of values
    # with the guessed value removed if it was present

    #If a lower number is guessed, you must print:
    #'The closest to [guess] is lower'
    #elif a higher number is guessed, you must print:
    #'The closest to [guess] is higher'
    #elif a number in the list is guessed, you must print:
    #'You found [guess]! It was in the list'
    #return values


def find_closest(guess, values):
    distance = 0
    closest = 0
    for x in values:
        current_distance = abs(guess - x)
        if distance == 0 or current_distance < distance:
            distance = current_distance
            closest = x

    # This function should return the closest value
    # to the guessed value
    return closest


def run_game(values):
    while(len(values) > 0):
        guess =input("enter a guess")
        if quess == 'q': break
        try:
            guess = int(guess)
        except ValueError:
            print("That's not an int!")
        values = handle_guess(guess, values)
    # While there are values to be guessed and the user hasn't
    # quit (with 'q', the game should continue to run, waiting
    # for user to input their guess.
    # This function exits when the game is over
    print('Thanks for playing! See you soon')

if __name__ == '__main__':
    values = sorted(random.sample(range(MIN, MAX+1), NUM_VALUES))
    run_game(values)
