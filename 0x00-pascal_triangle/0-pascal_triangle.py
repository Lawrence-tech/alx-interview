#!/usr/bin/python3
"""
    Returns a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    return a list of lists of integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    # Initialize the result list with the first row containing 1
    result = [[1]]

    for i in range(1, n):
        # Calculate the next row based on the previous row
        prev_row = result[-1]
        current_row = [1]  # First element is always 1
        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])
        current_row.append(1)  # Last element is always 1

        # Add the current row to the result list
        result.append(current_row)

    return result
