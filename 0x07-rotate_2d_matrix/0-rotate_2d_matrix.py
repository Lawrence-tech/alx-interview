#!/usr/bin/python3
"""
Module to  Rotate 2D Matrix
Requirement: Given an n x n 2D matrix, rotate it 90 degrees clockwise.
"""


def rotate_2d_matrix(matrix):
    """
    Rotate an n x n 2D matrix 90 degrees clockwise in-place.

    Args:
    matrix (List[List[int]]): The input matrix to be rotated.

    Returns:
    None: The matrix is modified in-place.
    """
    n = len(matrix)

    # Step 1: Transpose the matrix (swap rows and columns)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Step 2: Reverse each row of the transposed matrix
    for row in matrix:
        row.reverse()
