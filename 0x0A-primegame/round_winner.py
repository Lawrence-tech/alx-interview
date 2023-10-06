#!/usr/bin/python3
"""
Prime Game Round winner
"""
from check_prime_number import is_prime


def round_winner(n):
    """
    A function to determine the winner of 1 (a single) round

    Args:
        n - an integer value
    """
    # Maria starts first
    maria_turn = True
    prime_found = None

    while n > 1:
        prime_found = False

        # Find the largest prime number in the remaining range
        for i in range(n, 1, -1):
            if is_prime(i):
                prime_found = True
                n -= i  # Remove the prime number and its multiples
                break
        if not prime_found:
            break

        # Switch turns
        maria_turn = not maria_turn
    return "Maria" if maria_turn else "Ben"


if __name__ == "__main__":
    # Testing
    from random import randint

    """
    Create a list of ten randomly generated numbers
    from 0 to 99
    """
    test_list = [randint(0, 100) for i in range(10)]
    test_dict = {}

    for i in test_list:
        test_dict[i] = round_winner(i)

    """
    print out a dictionary with keys (integers)
    and values (strings)
    to indicate the winner of several rounds
    """
    print(test_dict)
    """
    {57: 'Maria', 38: 'Ben',
     25: 'Maria', 86: 'Maria',
     80: 'Ben', 2: 'Ben',
     24: 'Ben', 44: 'Ben',
     22: 'Maria', 36: 'Maria'
    }
    """
