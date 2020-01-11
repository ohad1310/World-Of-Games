from utils import *


def add_score(difficulty):
    try:
        scores = open(SCORES_FILE_NAME, 'r')
        scores = scores.read()
        if scores.isdecimal():
            scores_add = int(scores) + int(difficulty)
            scores_add = str(scores_add)
            scores = open(SCORES_FILE_NAME, 'w')
            scores.write(scores_add)
            scores.close()
            print(scores_add)
        else:
            scores = open(SCORES_FILE_NAME, 'w')
            scores.write(str(difficulty))
            scores.close()
    except IOError or FileNotFoundError:
        scores = open("scores.txt", 'a')
        scores.write(str(difficulty))
        scores.close()