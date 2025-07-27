# LEETCODE 209
"""Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose
sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""


def minSub(target, nums):
    n = len(nums)
    left = 0
    ans = float("inf")  # not zero because 0 > 2 answer = 0
    sum = 0

    for right in range(n):
        sum += nums[right]

        while sum >= target:
            ans = min(ans, right - left + 1)
            sum -= nums[left]
            left += 1

    return ans if ans != float("inf") else 0


print(minSub(target=7, nums=[2, 3, 1, 2, 4, 3]))
