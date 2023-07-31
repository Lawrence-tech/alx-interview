#!/usr/bin/python3

"""
A method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    function to determine behaviour of the boxes
    """
    if not boxes or len(boxes) == 0:
        return False

    # Initialize a list to keep track of visited boxes
    visited = [False] * len(boxes)
    visited[0] = True  # The first box is unlocked

    # Initialize a queue for BFS
    queue = [0]

    # Perform BFS
    while queue:
        current_box = queue.pop(0)

        # Check each key in the current box
        for key in boxes[current_box]:
            if key < len(boxes) and not visited[key]:
                visited[key] = True
                queue.append(key)

    # Check if all boxes were visited
    return all(visited)
