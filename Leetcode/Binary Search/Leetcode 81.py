# Search in Rotated Sorted Array II

"""There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting
array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7]
might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

You must decrease the overall operation steps as much as possible."""


class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True
            # Handle duplicates: when nums[left] == nums[mid] == nums[right]
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # Left half is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False


if __name__ == "__main__":
    obj = Solution()
    print(obj.search(nums=[1, 0, 1, 1, 1], target=0))


"""What was missing:
Rotation handling: You need to determine which half is sorted
Duplicate handling: When nums[left] == nums[mid] == nums[right], you can't determine which half is sorted, 
so you need to shrink the search space
Proper target range checks: You need to check if the target is within the sorted half's range"""
