# LEETCODE (medium)

"""Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place."""


def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    first_row_has_zero = False
    first_col_has_zero = False

    # If first row contains zero
    for c in range(cols):
        if matrix[0][c] == 0:
            first_row_has_zero = True
            break

    # If first col contains zero
    for r in range(rows):
        if matrix[r][0] == 0:
            first_col_has_zero = True
            break

    # If the first column contains zero
    for r in range(rows):
        if matrix[r][0] == 0:
            first_col_has_zero = True
            break

    # use the first row and column as a note
    for r in range(1, rows):
        for c in range(1, cols):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    # set the marked rows to zero
    for r in range(1, rows):
        if matrix[r][0] == 0:
            for c in range(1, cols):
                matrix[r][c] = 0

    # set the marked columns to zero
    for c in range(1, cols):
        if matrix[0][c] == 0:
            for r in range(1, rows):
                matrix[r][c] = 0

    # set the first row to zero
    if first_row_has_zero:
        for c in range(cols):
            matrix[0][c] = 0

    # set the first column to zero
    if first_col_has_zero:
        for r in range(rows):
            matrix[r][0] = 0

    return matrix


print(setZeroes(matrix=[[1, 1, 1], [1, 0, 1], [1, 1, 1]]))