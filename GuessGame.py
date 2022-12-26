from random import randint


def generate_number(difficulty):
    return randint(1, difficulty)


def get_guess_from_user(difficulty):
    return input(f'please guess a number between 1 and {difficulty}\n')


def compare_results(secret_number, user_guess):
    return secret_number == int(user_guess)


def play(difficulty):
    secret_number = generate_number(difficulty)
    user_guess = get_guess_from_user(difficulty)
    if user_guess.isdigit() and 1 <= int(user_guess) <= difficulty:
        return compare_results(secret_number, user_guess)
    print('wrong value')
    return

