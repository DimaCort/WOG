# should be run through terminal and not pycharm console, otherwise the screen clear dosnt work
import CurrencyRouletteGame
import GuessGame
import MemoryGame
from Live import load_game, welcome
import Utils
from Score import add_score


def launch():
    print(welcome("Guy"))
    game_num, game_def = load_game()
    if game_num == -1 or game_def == -1:
        print('you have entered wrong values, so im gonna crash')
    else:
        Utils.Screen_cleaner()
        match game_num:
            case 1:
                res = 'win' if MemoryGame.play(game_def) else 'lose'
            case 2:
                res = 'win' if GuessGame.play(game_def) else 'lose'
            case 3:
                res = 'win' if CurrencyRouletteGame.play(game_def) else 'lose'
        print(res)
        add_score(game_def)
        play_again = int(input('would you like to play again? type 1 for main menu, 0 if you want to quit\n'))
        if play_again:
            launch()


launch()
