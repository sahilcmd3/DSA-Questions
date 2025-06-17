# LEETCODE 974

"""Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
A subarray is a contiguous part of an array."""


# Brute Force
# Time Complexity: O(n^2)
# TLE
def subArrDiv(nums, k):
    pref_arr = [0] * (len(nums) + 1)

    for i in range(len(nums)):
        pref_arr[i] = nums[i] + pref_arr[i - 1]

    count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if (pref_arr[j + 1] - pref_arr[i]) % k == 0:
                count += 1

    return count


# Time Complexity: O(n)
# Prefix sum with map for edge cases and better modulo performance
def subArrDivHash(nums, k):
    count = 0
    pref_sum = 0
    rem_map = {0 : 1}

    for num in nums:
        pref_sum += num
        rem = pref_sum % k

        if rem < 0:
            rem += k

        count += rem_map.get(rem, 0)

        rem_map[rem] = rem_map.get(rem, 0) + 1

    return count


if __name__ == "__main__":
    # print(subArrDiv(nums=[4, 5, 0, -2, -3, 1], k=5))
    print(subArrDivHash(nums=[4, 5, 0, -2, -3, 1], k=5))
