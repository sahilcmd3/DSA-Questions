# LEETCODE 852

"""You are given an integer mountain array arr of length n where the values increase to a peak element and then decrease.
Return the index of the peak element.
Your task is to solve it in O(log(n)) time complexity."""


# Time Complexity: O(log n)
def peakMIA(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] > arr[mid + 1]:
            right = mid  # Peak is at mid or at left
        else:
            left = mid + 1  # Peak is to the right
    return left


print(peakMIA(arr=[0, 1, 0]))
