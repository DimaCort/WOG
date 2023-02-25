import os
import Utils


def add_score(game_def):
    if not os.path.isfile(Utils.SCORES_FILE_NAME):
        with open(Utils.SCORES_FILE_NAME, 'w') as f:
            f.write('0')
    with open(Utils.SCORES_FILE_NAME, 'r') as f:
        curr_score = int(f.read())
    curr_score += game_def * 3 + 5
    with open(Utils.SCORES_FILE_NAME, 'w') as f:
        f.write(str(curr_score))

