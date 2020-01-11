import os
import time

SCORES_FILE_NAME = "scores.txt"
ERROR_MESSAGE = "Something went wrong.."


def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')


def clean_above():
    time.sleep(0.7)
    screen_cleaner()