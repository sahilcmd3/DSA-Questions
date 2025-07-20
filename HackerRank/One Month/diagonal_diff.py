# Given a square matrix, calculate the absolute difference between the sums of its diagonals.


def diagonal(arr):
    sum_d1 = sum([arr[i][i] for i in range(0, len(arr))])
    sum_d2 = sum([arr[i][len(arr) - i - 1] for i in range(0, len(arr))])

    return abs(sum_d1 - sum_d2)
