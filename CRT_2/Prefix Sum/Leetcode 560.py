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
