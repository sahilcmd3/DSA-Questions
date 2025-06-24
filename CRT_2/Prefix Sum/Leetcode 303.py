# LEETCODE 303
"""Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive 
(i.e. nums[left] + nums[left + 1] + ... + nums[right])."""


class NumArray:
    # Time Complexity: O(n) (Pre-processing)
    def __init__(self, nums):
        self.prefix_nums = [0] * len(nums)
        self.prefix_nums[0] = nums[0]

        for i in range(1, len(nums)):
            self.prefix_nums[i] = nums[i] + self.prefix_nums[i - 1]
            
    # Time Complexity: O(1) (Querying)
    def sumRange(self, left, right):
        if left == 0:
            return self.prefix_nums[right]

        return self.prefix_nums[right] - self.prefix_nums[left - 1]


if __name__ == "__main__":
    numArray = NumArray(nums=[-2, 0, 3, -5, 2, -1])
    print(numArray.sumRange(0, 2))
    print(numArray.sumRange(2, 5))
    print(numArray.sumRange(0, 5))
