import os

SCORES_FILE_NAME = "Scores.txt"
BAD_RETURN_CODE = -1


def Screen_cleaner():
    os.system('cls')


def get_score():
    if os.path.isfile(SCORES_FILE_NAME):
        with open(SCORES_FILE_NAME, 'r') as f:
            score = f.read()
        return score
    else:
        return BAD_RETURN_CODE


