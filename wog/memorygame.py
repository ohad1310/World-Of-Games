import random
from utils import clean_above


def generate_sequence(difficulty):
    list_a = []
    for j in range(int(difficulty)):
        list_a.append(random.randint(1, 101))
    print(list_a)
    clean_above()
    return list_a


def get_list_from_user(difficulty):
    print('After seeing the numbers enter the numbers you saw, each one separated with Enter.')
    list_b = []
    for i in range(int(difficulty)):
        list_b.append(int(input()))
    print(list_b)
    return list_b


def is_list_equal(list_a, list_b):
    if list_a == list_b:
        print("you are correct")
        return True
    else:
        print('You are WRONG')
        return False


def play(difficulty):
    return is_list_equal(generate_sequence(difficulty), get_list_from_user(difficulty))