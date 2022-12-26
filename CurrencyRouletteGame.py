from random import randint
from currency_converter import CurrencyConverter


def get_money_interval(difficulty):
    usd_amount = randint(1, 100)
    ils_amount = CurrencyConverter().convert(usd_amount, 'USD', 'ILS')
    interval_low = ils_amount - (5 - difficulty)
    interval_high = ils_amount + (5 - difficulty)
    return usd_amount, interval_low, interval_high


def get_guess_from_user(usd_amount):
    user_guess = input(f'how much is {usd_amount}USD in ILS?\n')
    return int(user_guess)


def play(difficulty):
    usd_amount, interval_low, interval_high = get_money_interval(difficulty)
    user_guess = get_guess_from_user(usd_amount)
    return interval_low <= user_guess <= interval_high
