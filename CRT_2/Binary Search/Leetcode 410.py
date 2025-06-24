# LEETCODE 410
"""Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.
Return the minimized largest sum of the split.
A subarray is a contiguous part of the array."""


def splitArray(nums, k):
    def can_split(max_sum_allowed):
        count = 1
        current_sum = 0
        for num in nums:
            if current_sum + num > max_sum_allowed:
                count += 1
                current_sum = num
            else:
                current_sum += num
        return count <= k

    low, high = max(nums), sum(nums)
    result = high

    while low <= high:
        mid = (low + high) // 2
        if can_split(mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


print(splitArray(nums=[7, 2, 5, 10, 8], k=2))
