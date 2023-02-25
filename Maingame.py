# should be run through terminal and not the pycharm console, otherwise the screen clear dosnt work
from games import CurrencyRouletteGame, GuessGame, MemoryGame
from Live import load_game, welcome
import Utils
from Score import add_score


def launch(name):
    print(welcome(name))
    game_num, game_def = load_game()
    while game_num == -1 or game_def == -1:
        Utils.Screen_cleaner()
        input('you have entered wrong values, press any key to try again')
        game_num, game_def = load_game()
    match game_num:
        case 1:
            res = 'win' if MemoryGame.play(game_def) else 'lose'
        case 2:
            res = 'win' if GuessGame.play(game_def) else 'lose'
        case 3:
            res = 'win' if CurrencyRouletteGame.play(game_def) else 'lose'
    Utils.Screen_cleaner()
    print(res)
    add_score(game_def)
    play_again = int(input('would you like to play again? type 1 for main menu, 0 if you want to quit\n'))
    if play_again:
        Utils.Screen_cleaner()
        launch(name)

player = input('Please enter your name: \n')
Utils.Screen_cleaner()
launch(player)
