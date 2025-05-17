# LEETCODE

"""You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive).

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of
nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

Meaning: Create new lists for consecutive numbers"""


# Time Complexity: O(n)
def sumRange(nums):
    result = []  # To store final result

    if not nums:  # For empty list
        return result

    start = nums[0]

    for i in range(1, len(nums) + 1):
        if i == len(nums) or nums[i] != nums[i - 1] + 1:  # checks for next consecutive number if not then closes the range
            if start == nums[i - 1]:
                result.append(str(start))  # For single number
            else:
                result.append(f"{start} -> {nums[i-1]}")  # Format to print ranges

            if i < len(nums):  # For new ranges
                start = nums[i]

    return result


print(sumRange(nums=[0, 1, 2, 4, 5, 7]))