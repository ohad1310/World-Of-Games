from live import *
from utils import *
from guessgame import play as guess_play
from memorygame import play as memory_game
from score import *
from mainscores import score_server


def main():
    name = input('Please enter your name:')
    print(welcome(name))
    game_result = False
    while game_result is False:
        screen_cleaner()
        game, difficulty = load_game()
        if game == "1":
            game_result = memory_game(difficulty)
        elif game == "2":
            game_result = guess_play(difficulty)
    while game_result is True:
        screen_cleaner()
        add_score(difficulty)
        score_server(difficulty)
        game, difficulty = load_game()
        if game == "1":
            game_result = memory_game(difficulty)
        elif game == "2":
            game_result = guess_play(difficulty)


if __name__ == '__main__':
    main()