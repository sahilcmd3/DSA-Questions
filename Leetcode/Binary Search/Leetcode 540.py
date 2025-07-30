# Single Element in a Sorted Array

"""You are given a sorted array consisting of only integers where every element appears exactly twice, except for one
element which appears exactly once.
Return the single element that appears only once.
Your solution must run in O(log n) time and O(1) space."""


class Solution:
    def single(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if mid % 2 == 1:
                mid -= 1
            if nums[mid] != nums[mid + 1]:
                right = mid
            else:
                left = mid + 2

        return nums[left]


if __name__ == "__main__":
    obj = Solution()
    print(obj.single(nums=[1, 1, 2, 3, 3, 4, 4, 8, 8]))
