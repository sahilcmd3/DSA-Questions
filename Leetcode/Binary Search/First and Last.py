# LEETCODE 34

"""Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity."""


# Time Complexity: O(log n)
class Solution:
    def binSearch(self, nums, target, is_searching_left):
        left = 0
        right = len(nums) - 1
        idx = -1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                idx = mid
                if is_searching_left:
                    right = mid - 1
                else:
                    left = mid + 1

        return idx

    def searchRange(self, nums, target):
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)

        return [left, right]


if __name__ == "__main__":
    obj = Solution()
    print(obj.searchRange(nums=[5, 7, 7, 8, 8, 10], target=8))
