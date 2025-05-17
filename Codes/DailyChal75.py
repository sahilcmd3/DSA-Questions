# LEETCODE (medium)

"""Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color
are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function."""


# Dutch National Flag alogrithm
# Dutch national flag problem (red, white, blue)=(0, 1, 2)
# Set 3 pointers l<=m<=r to partition the array
# Use a conditional loop while m<=r check nums[m]


# Time Complexity: O(nums)
def sortColor(nums):
    red, white, blue = 0, 1, 2
    l, m, r = 0, 0, len(nums) - 1

    while m <= r:
        if nums[m] == red:
            nums[l], nums[m] = nums[m], nums[l]
            l += 1
            m += 1
        elif nums[m] == white:
            m += 1
        else:
            nums[m], nums[r] = nums[r], nums[m]
            r -= 1

    return nums


print(sortColor(nums=[2, 0, 2, 1, 1, 0]))