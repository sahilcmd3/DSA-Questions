# LEETCODE and NEETCODE

"""Given an array of integers nums and an integer target, return indices of the two numbers such that
they add up to target."""


# Time complexity: O(N^2)
"""def two_sum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if target == nums[i] + nums[j]:
                return [i, j]


nums = [2, 7, 11, 15]
target = 13
a = two_sum(nums, target)
print(f'Index of numbers resulting target are: {a}')"""


# Two Pointer approach
# Needs sorted array
# Time complexity: sorting + tow pointers: O(n * log n)
"""def twoSum(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        sum = nums[left] + nums[right]
        if sum == target:
            return [left, right]
        elif sum < target:
            left += 1
        else:
            right -= 1

    return False


print(twoSum(nums=[2, 7, 11, 15], target=9))"""


# Hashmap approach
# Time complexity: O(nums)
def twoSum(nums, target):
    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

    return False


print(twoSum(nums=[3, 2, 4], target=6))