# LEETCODE 1752

# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of
# positions (including zero). Otherwise, return false.
# There may be duplicates in the original array.

# Note: An array A rotated by x positions results in an array B of the same length such that B[i] == A[(i+x) % A.length] for every 
# valid index i.


class Solution:
    """Check if array is sorted and rotated.
    The key insight is that in a sorted and rotated array, there can be
    at most one position where nums[i] > nums[i+1] (the rotation point)."""

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def check(self, nums):
        n = len(nums)
        rotation_points = 0

        # Count how many times we have nums[i] > nums[(i+1) % n]
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                rotation_points += 1

        # If there's at most 1 rotation point, the array is sorted and rotated
        return rotation_points <= 1


if __name__ == "__main__":
    obj = Solution()
    print(obj.check(nums=[3, 4, 5, 1, 2]))
