# LEETCODE 283
"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array."""


# Two pointer approach
# Time complexity: O(n)
def moveZereos(nums):
    left = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1

    return nums


print(moveZereos(nums=[0, 1, 0, 3, 12]))
