# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the
# five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.


def miniMax(arr):
    total_sum = sum(arr)

    min_sum = total_sum - max(arr)
    max_sum = total_sum - min(arr)

    print(min_sum, max_sum)


if __name__ == "__main__":
    miniMax(arr=[1, 3, 5, 7, 9])
