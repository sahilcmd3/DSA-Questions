# LEETCODE (Daily challenge)

"""Given an array nums of integers, return how many of them contain an even number of digits."""


# Time complexity: O(num)
def findnums(nums):
    res = 0

    for num in nums:
        if 9 < num < 100 or 999 < num < 10000 or num == 100000:
            res += 1

    return res


print(findnums(nums = [12, 345, 2, 6, 7896]))


# Approach
""" Even digits from 1 to 100000 should be
        1. 10 - 99
        2. 1000 - 9999
        3. 100000 """