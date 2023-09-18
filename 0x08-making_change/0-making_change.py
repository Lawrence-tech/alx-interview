#!/usr/bin/python3
"""
Module to Return: fewest number of coins needed to meet total
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Create a list to store the min no of coins for @ amount from 0 to total
    # Initialize all values to infinity except for 0, which is 0 coins needed
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    if dp[total] == float('inf'):
        return -1

    return dp[total]


# Example usage:
if __name__ == "__main__":
    coins = [1, 2, 5]
    total = 11
    result = makeChange(coins, total)
    print(f"The fewest number of coins needed to make {total} is {result}")
