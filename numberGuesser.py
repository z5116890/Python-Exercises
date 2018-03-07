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
    # complete your solution here
    # This function should return a duplicate list of values
    # with the guessed value removed if it was present
    return values


def find_closest(guess, values):
    # This function should return the closest value
    # to the guessed value
    pass


def run_game(values):
    guess = None
    # While there are values to be guessed and the user hasn't
    # quit (with 'q', the game should continue to run, waiting
    # for user to input their guess.
    # This function exits when the game is over
    print('Thanks for playing! See you soon')

if __name__ == '__main__':
    values = sorted(random.sample(range(MIN, MAX+1), NUM_VALUES))
    run_game(values)
