# STRIVER (LEETCODE)

"""Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]"""


# Recursion Approach
#     Base case: If numRows is 1, return [[1]].
#     Recursively generate the triangle for numRows - 1.
#     Calculate the current row by summing adjacent elements from the previous row.


# Time complexity: O(rows^2)
def pas(rows):
    if rows == 0:
        return []
    if rows == 1:
        return [[1]]

    prevRows = pas(rows - 1)
    newRow = [1] * rows

    for i in range(1, rows - 1):
        newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]

    prevRows.append(newRow)
    return prevRows


print(pas(rows=5))