# LEETCODE 977
"""Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order."""


# Two pointer approach
# Time Complexity: O(n)
def sortedSquares(nums):
    n = len(nums)
    answer = [0] * n

    left = 0
    right = n - 1

    for i in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            answer[i] = nums[left] ** 2
            left += 1
        else:
            answer[i] = nums[right] ** 2
            right -= 1

    return answer


print(sortedSquares(nums=[-4, -1, 0, 3, 10]))
