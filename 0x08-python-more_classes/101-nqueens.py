#!/usr/bin/python3
"""The Nqueen program"""

import sys


def is_safe(board, row, col):
    """
    Checks for the safe position to place the queen
    """
    # Check if it's safe to place a queen at board[row][col]
    n = len(board)

    # Check the column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(n):
    """
    Function to solve the nqueen
    """
    def solve(board, row):
        """
        Solves for the row
        """
        if row == n:
            solutions.append(
                ["".join(["Q" if cell == 1 else "." for cell in row])
                    for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve(board, row + 1)
                board[row][col] = 0

    solutions = []
    board = [[0] * n for _ in range(n)]
    solve(board, 0)
    return solutions


def print_solutions(solutions):
    """
    This prints the nqueen solution
    """
    for solution in solutions:
        for row in solution:
            print(row)
        print()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_n_queens(n)
    print_solutions(solutions)
