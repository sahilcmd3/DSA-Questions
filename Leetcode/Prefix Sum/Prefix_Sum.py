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


if __name__ == "__main__":
    print(runSum(nums=[1, 2, 3, 4]))
