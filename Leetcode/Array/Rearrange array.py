# LEETCODE 2149

"""You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should return the array of nums such that the the array follows the given conditions:

    Every consecutive pair of integers have opposite signs.
    For all integers with the same sign, the order in which they were present in nums is preserved.
    The rearranged array begins with a positive integer.

Return the modified array after rearranging the elements to satisfy the aforementioned conditions."""


# Time complexity: O(n)
def rearrange(nums):
    pi = 0
    ni = 1
    res = [0] * len(nums)
    
    for n in nums:
        if n > 0:
            res[pi] = n
            pi += 2
        else:
            res[ni] = n
            ni += 2
    
    return res

if __name__ == "__main__":
    print(rearrange(nums=[3,1,-2,-5,2,-4]))