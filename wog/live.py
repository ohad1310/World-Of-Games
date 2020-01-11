from utils import *


def welcome(name):
    return "Hello {} and welcome to World Of Games (WOG).\nHere you can find many cool games to play!".format(name)


def load_game():
    game = input('Please choose a game to play:\n   1. Memory Game - a sequence of numbers will appear for 1 second and'
                 'you have to guess it back\n   2. Guess Game - guess a number and see if you chose like the computer\n')
    difficulty = input('Please choose difficulty level from 1 - 5\n')

    if game == '1' or game == '2':
        print('Good')
    else:
        raise Exception(ERROR_MESSAGE)

    list_difficulty = ['1', '2', '3', '4', '5']
    if difficulty in list_difficulty:
        print("Difficulty: " + difficulty)
    else:
        raise Exception(ERROR_MESSAGE)

    return game, difficulty
