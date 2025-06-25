# LEETCODE 169

"""Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""


# Time Complexity: O(n^2)
def majorEle(nums):
    n = len(nums)

    for i in set(nums):
        if nums.count(i) > n // 2:
            return i


# Time Complexity: O(n log n)
def majorELEM(nums):
    nums.sort()
    n = len(nums)
    return nums[n // 2]


if __name__ == "__main__":
    print(majorELEM(nums=[2, 1, 2, 2, 2, 1]))
