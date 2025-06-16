"""A prefix sum is calculated by creating another array same size of the given array (n). where new array is pre and given is nums
   create a new pre array (pre_nums=[0]*n) where n is the size of the array
        
        pre[i]=nums[i]+pre[i-1]"""



# LEETCODE 1480
"""Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]

Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4]."""


# Time Complexity: O(n)
def runSum(nums):
    n = len(nums)
    pre_nums = [0] * n
    pre_nums[0] = nums[0]

    for i in range(1, n):
        pre_nums[i] = nums[i] + pre_nums[i - 1]

    return pre_nums


"""Another Approach (in-place approach)
def runSum(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]"""


#if __name__ == "__main__":
    #print(runSum(nums=[1, 2, 3, 4]))



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


"""if __name__ == "__main__":
    numArray = NumArray(nums=[-2, 0, 3, -5, 2, -1])
    print(numArray.sumRange(0, 2))
    print(numArray.sumRange(2, 5))
    print(numArray.sumRange(0, 5))"""



# LEETCODE 560
"""Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
A subarray is a contiguous non-empty sequence of elements within an array."""


# Time Complexity: O(n)
def subarraysum(nums, k):
    pre = [0] * len(nums)
    pre[0] = nums[0]
    count = 0
    prefix_map = {0 : 1}
    
    for i in range(len(nums)):
        if i > 0:
            pre[i] = nums[i] + pre[i-1]
        
        count += prefix_map.get(pre[i] - k, 0)
        
        prefix_map[pre[i]] = prefix_map.get(pre[i], 0) + 1
    
    return count


if __name__ == "__main__":
    print(subarraysum(nums=[1,1,1], k = 2))
