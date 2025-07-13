# Given an array, we have to find the largest element in the array.


def largest(arr):
    n = len(arr)
    max = arr[0]

    for i in range(0, n):
        if max < arr[i]:
            max = arr[i]

    return max


print(largest(arr=[2, 5, 1, 3, 0]))
