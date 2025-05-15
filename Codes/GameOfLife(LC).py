# LEETCODE (medium)

"""The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or
dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the
following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the current
state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state."""


def game(board):
    m = len(board)
    n = len(board[0])

    for i in range(m):
        for j in range(n):
            ones = 0

            for x in range(max(0, i-1)), min(m, i+2):
                for y in range(max(0, j-1), min(n, j+2)):
                    ones += board[x][y] & 1

            if board[i][j] == 1 and (ones == 3 or ones == 4):
                board[i][j] |= 0b10
                if board[i][j] == 0 and ones == 3:
                    board[i][j] |= 0b10

    for i in range(m):
        for j in range(n):
            board[i][j] >>= 1


print(game(board=[[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))