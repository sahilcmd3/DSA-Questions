# LEETCODE (medium)

"""You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation."""


def rotate(matrix):
    edge_len = len(matrix)
    top = 0
    bottom = edge_len - 1

    while top < bottom:
        for col in range(edge_len):
            temp = matrix[top][col]
            matrix[top][col] = matrix[bottom][col]
            matrix[bottom][col] = temp

        top += 1
        bottom -= 1

    for row in range(edge_len):
        for col in range(row + 1, edge_len):
            temp = matrix[row][col]
            matrix[row][col] = matrix[col][row]
            matrix[col][row] = temp

    return matrix


print(rotate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
