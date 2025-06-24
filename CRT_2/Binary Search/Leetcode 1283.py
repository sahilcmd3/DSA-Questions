# LEETCODE 1283
"""Given an array of integers nums and an integer threshold, we will choose a positive integer divisor, divide all the array by
it, and sum the division's result. Find the smallest divisor such that the result mentioned above is less than or equal to threshold.
Each result of the division is rounded to the nearest integer greater than or equal to that element. (For example: 7/3 = 3 and 10/2 = 5).
The test cases are generated so that there will be an answer."""

import math


# Time COmplexity: O(Nlog(Max(Nums)))
def smallestDivisor(nums, threshold):

    def compute_sum(divisor):
        return sum(math.ceil(num / divisor) for num in nums)

    left = 1
    right = max(nums)

    while left < right:
        mid = (left + right) // 2
        if compute_sum(mid) <= threshold:
            right = mid
        else:
            left = mid + 1

    return left


print(smallestDivisor(nums=[1, 2, 5, 9], threshold=6))
