#!/usr/bin/python3
"""
Module def island_perimeter(grid): that returns the perimeter of the island
"""


def island_perimeter(grid):
    perimeter = 0
    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Initialize with 4 sides (top, bottom, left,

                # Check and subtract for adjacent land cells
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1  # Subtract top side
                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1  # Subtract bottom side
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1  # Subtract left side
                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1  # Subtract right side

    return perimeter


# Test the function with the provided grid
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))
