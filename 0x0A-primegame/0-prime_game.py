#!/usr/bin/python3
"""
Prime Interview Game Challenge Module
"""


def isWinner(x, nums):
    """
    Function to determine the winner of a game after x rounds
    """
    def sieve_of_eratosthenes(n):
        """
        Use to find prime numbers and calculates the winner based on the count
        """
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False
        primes = []

        for p in range(2, n + 1):
            if is_prime[p]:
                primes.append(p)
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False

        return primes

    def calculate_winner(n):
        """
        Determine the winner of a single round
        """
        primes = sieve_of_eratosthenes(n)
        if len(primes) % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if n <= 1:
            continue
        winner = calculate_winner(n)
        if winner == "Ben":
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
