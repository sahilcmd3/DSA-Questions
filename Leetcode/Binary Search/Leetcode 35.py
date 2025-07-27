# LEETCODE 35
"""Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the
index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity."""


# Time Complexity: O(log n)
def sip(nums, target):
    left, right = 0, len(nums)

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


print(sip(nums=[1, 3, 5, 6], target=5))
