# LEETCODE

"""Given a 0-indexed integer array nums of size n, find the maximum difference between nums[i] and nums[j] (i.e., nums[j] - nums[i]),
such that 0 <= i < j < n and nums[i] < nums[j].

Return the maximum difference. If no such i and j exists, return -1."""


# Time Complexity: O(n)
def maximumDiff(nums):
    min_val = nums[0]
    max_diff = -1

    for i in range(1, len(nums)):
        if nums[i] > min_val:
            max_diff = max(max_diff, nums[i] - min_val)
        else:
            min_val = nums[i]

    return max_diff


print(maximumDiff(nums=[7, 1, 5, 4]))
