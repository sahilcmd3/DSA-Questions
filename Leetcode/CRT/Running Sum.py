# LEETCODE

"""Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums."""


# Time complexity: O(n)
def runningSum(nums):
    output = [0] * len(nums)  # An output array which stores the value same as nums
    output[0] = nums[0]  # Assigning output index value same as nums
    for idx in range(1, len(nums)):
        output[idx] = output[idx - 1] + nums[idx]  # Assigning values to output
    return output


print(runningSum(nums=[1, 2, 3, 4]))