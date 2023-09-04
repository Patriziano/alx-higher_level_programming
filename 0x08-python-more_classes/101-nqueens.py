#!/usr/bin/python3
"""The Nqueen program"""

import sys


def is_safe(board, row, col):
    """
    Checks where is safe to place the queen
    """
    # If there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

# If queen is in the upper left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

# If a queen is in the upper right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(n):
    """
    the function that solves the position to place the solution
    """

    board = [['.' for _ in range(n)] for _ in range(n)]
    solutions = []

    def backtrack(row):
        """
        The backtrack function
        """
        nonlocal solutions

        if row == n:
            # Found a solution, add it to the list of solutions
            solutions.append([''.join(row) for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                backtrack(row + 1)
                board[row][col] = '.'

    backtrack(0)

    return solutions


def main():
    """
    The main program
    """

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Solve the N-queens problem
    solutions = solve_nqueens(n)

    for solution in solutions:
        for row in solution:
            print(row)
        print()


if __name__ == "__main__":
    main()
