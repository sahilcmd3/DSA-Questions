# Find Peak element

"""A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return
the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a
neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time."""


# Time Complexity: O(log n)
class Solution:
    def findPeak(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    obj = Solution()
    print(obj.findPeak(nums=[1, 2, 3, 1]))
