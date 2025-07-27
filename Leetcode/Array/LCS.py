# LEETCODE

"""Given an array nums of n integers, return the length of the longest sequence of consecutive integers. The integers in
this sequence can appear in any order."""


# Solution using sorting.
# Time Complexity: O(n log n)
# Space Complexity: O(1) if sorting in-place
def conse(nums):
    if not nums:
        return 0

    nums = sorted(set(nums))

    longest = 1
    current_length = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            current_length += 1
        else:
            longest = max(longest, current_length)
            current_length = 1

    return max(longest, current_length)


if __name__ == "__main__":
    print(conse(nums=[100, 4, 200, 1, 3, 2]))
