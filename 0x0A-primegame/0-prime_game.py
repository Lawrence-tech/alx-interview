#!/usr/bin/python3
"""
Prime Game Module
"""


def isWinner(x, nums):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def calculate_primes_sieve(n):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        p = 2
        while p * p <= n:
            if sieve[p]:
                for i in range(p * p, n + 1, p):
                    sieve[i] = False
            p += 1
        primes = [i for i in range(2, n + 1) if sieve[i]]
        return primes

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes = calculate_primes_sieve(n)
        prime_count = len(primes)

        if prime_count == 0:
            continue
        elif prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
