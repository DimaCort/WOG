from random import randint
from time import sleep
import Utils


def generate_sequence(difficulty):
    lst = [None] * difficulty
    for i in range(difficulty):
        lst[i] = randint(1, 101)
    return lst


def get_list_from_user(difficulty):
    lst = [None] * difficulty
    print('please enter the list number you just saw\n')
    for i in range(difficulty):
        lst[i] = int(input())
    return lst


def is_list_equal(generate_lst, user_lst):
    return generate_lst == user_lst


def play(difficulty):
    generate_lst = generate_sequence(difficulty)
    print(generate_lst)
    sleep(1)
    Utils.Screen_cleaner()
    user_lst = get_list_from_user(difficulty)
    return is_list_equal(generate_lst, user_lst)
