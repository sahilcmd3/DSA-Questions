# LEETCODE 136

"""Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
"""


# Time Complexity: O(n)
# Space Complexity: O(1)
def singleNum(nums):
    xor = 0

    for num in nums:
        xor ^= num

    return xor


if __name__ == "__main__":
    print(singleNum(nums = [2,2,1]))
