import random


def generate_number(difficulty):
    secret_number = random.randint(1, int(difficulty))
    return secret_number


def get_guess_from_user(difficulty):
    usr_guess = input("Guess a number between 1 to {}?\n".format(difficulty))
    return int(usr_guess)


def compare_results(secret_number, usr_guess):
    if secret_number == usr_guess:
        print("you are correct")
        return True
    else:
        print('You are WRONG')
        return False


def play(difficulty):
    return compare_results(generate_number(difficulty), get_guess_from_user(difficulty))


