#LEETCODE (medium)

"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the
elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation."""


#Time Complexity: O(n)
def product(nums):

    hashmap = {} # The value_map stores the original values from nums, retrieve them after modifying nums during the
    # prefix and suffix calculations.

    for i in range(len(nums)):
        hashmap[i] = nums[i]

    prefix = 1
    for i in range(len(nums)):
        current_value = nums[i]
        nums[i] = prefix
        prefix *= current_value
        """The nums array is updated in-place to store the prefix product at each index. For example:
           Before: nums = [1, 2, 3, 4]
           After prefix pass: nums = [1, 1, 2, 6]"""

    suffix = 1
    for i in range(len(nums) - 1, -1, -1):
        nums[i] *= suffix
        suffix *= hashmap[i]
        """The nums array is then further updated by multiplying each value with the suffix product, 
           which is computed in reverse order. For example:
           After suffix pass: nums = [24, 12, 8, 6]"""

    return nums


nums = [1, 2, 3, 4]  #Output = [24,12,8,6]
ans = (product(nums))
print(ans)