# LEETCODE and NEETCODE

"""Given an array of integers nums and an integer target, return indices of the two numbers such that
they add up to target."""

def two_sum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if target == nums[i] + nums[j]:
                return [i, j]


nums = [2, 7, 11, 15]
target = 13
a = two_sum(nums, target)
print(f'Index of numbers resulting target are: {a}')