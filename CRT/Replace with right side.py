# LEETCODE (medium)

"""Given an array arr, replace every element in that array with the greatest element among the elements to its right,
and replace the last element with -1.
After doing so, return the array."""


def replaceElements(arr):
    n = len(arr)
    maxRight = -1  # Initialize the maximum element on the right as -1

    # Traverse the array from right to left
    for i in range(n - 1, -1, -1):
        # Store the current element before it gets overwritten
        current = arr[i]
        # Replace the current element with the max element to its right
        arr[i] = maxRight
        # Update the maxRight with the maximum of current and maxRight
        maxRight = max(maxRight, current)

    return arr


print(replaceElements(arr=[17, 18, 5, 4, 6, 1]))