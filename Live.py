
def welcome(name):
    return f'Hello {name} and welcome to the World of Games (WoG).\nHere you can find many cool games to play.'

def load_game():
    game_num = input('''Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
    2. Guess Game - guess a number and see if you chose like the computer.
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS.\n''')
    game_def = input('Please choose game difficulty from 1 to 5:\n')
    if not (game_num.isdigit() and game_def.isdigit()):
        return -1, -1
    if not (1 <= int(game_num) <= 3 and 1 <= int(game_def) <= 5):
        return -1, -1
    return int(game_num), int(game_def)