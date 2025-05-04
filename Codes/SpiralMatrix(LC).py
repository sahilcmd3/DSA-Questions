# LEETCODE (medium)

"""Given an m x n matrix, return all elements of the matrix in spiral order."""


# Time Complexity: O(rows * cols)
def spiralOrder(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    x, y, dx, dy = 0, 0, 1, 0
    res = []

    for _ in range(rows * cols):
        res.append(matrix[y][x])
        matrix[y][x] = "."

        if not 0 <= x + dx < cols or not 0 <= y + dy < rows or matrix[y + dy][x + dx] == ".":
            dx, dy = -dy, dx

        x += dx
        y += dy

    return res


print(spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
