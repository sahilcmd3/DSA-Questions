#LEETCODE

"""Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
if k=2 I have to rotate the array k times"""

#Time complexity: O(K∗N)
def rotate (nums,k):
    k=k%len(nums)
    for i in range(k):
        nums.insert(0, nums.pop()) #index is starting from zero pop and put
    return nums
nums=[1,2,3,4,5,6,7]
k=3
a=rotate(nums,k)
print(a)

#Time Complexity: O(n)
def rotate(nums, k):
    n = len(nums)
    k = k % n  # In case k is greater than the length of the array
    nums[:] = nums[-k:] + nums[:-k]  # Rotate the array
    """If nums = [1, 2, 3, 4, 5, 6, 7] and k = 3, here's how the line works:
       nums[-3:] gives [5, 6, 7]
       nums[:-3] gives [1, 2, 3, 4]
       Concatenating them gives [5, 6, 7, 1, 2, 3, 4]
       nums[:] = [5, 6, 7, 1, 2, 3, 4] updates the original list.
       So, the array [1, 2, 3, 4, 5, 6, 7] is rotated 3 steps to the right, resulting in [5, 6, 7, 1, 2, 3, 4]."""
    return nums

# Example usage
print(rotate([1, 2, 3, 4, 5, 6, 7], 3))