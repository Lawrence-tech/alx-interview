#!/usr/bin/python3
"""
Prime Game Interview Module
"""
from round_winner import round_winner


def isWinner(x, num):
    """
    Function to determine the winner of the game,
    after x number of rounds
    """
    ben, maria = 0, 0

    for i in range(x):
        # The winner of each round gets 1 (a single) point
        winner = round_winner(num[i])
        if winner == "Ben":
            ben += 1
        elif winner == "Maria":
            maria += 1

    # The player with the highest points after a full game wins
    # The both playes get same or no points, there is no winner (None)
    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
