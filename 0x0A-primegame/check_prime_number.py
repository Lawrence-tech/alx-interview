#!/usr/bin/python3
"""
Prime Game Helper function Module
"""


def is_prime(num):
    """
    A helper function to determine if a number is prime or not

    Args:
        num - an integer value
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if (num % i) == 0:
            return False
    return True


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
        test_dict[i] = is_prime(i)

    """
    print out a dictionary with keys (integers)
    and values (booleans)
    to indicate whether integer is a prime number or not
    """
    print(test_dict)
    """
    {14: False, 67: True,
     52: False, 51: False,
     85: False, 56: False,
     88: False, 5: True
    }
    """
