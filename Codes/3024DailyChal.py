# LEETCODE

"""You are given a 0-indexed integer array nums of size 3 which can form the sides of a triangle.

A triangle is called equilateral if it has all sides of equal length.
A triangle is called isosceles if it has exactly two sides of equal length.
A triangle is called scalene if all its sides are of different lengths.
Return a string representing the type of triangle that can be formed or "none" if it cannot form a triangle.
"""


# Time Complexity: O(1)
# Space Complexity: O(1)
def triangletypes(nums):
    nums.sort()

    if nums[2] >= nums[0] + nums[1]:
        return None
    elif nums[0] == nums[2]:
        return "equilateral"
    elif nums[0] == nums[1] or nums[1] == nums[2]:
        return "isosceles"
    else:
        return "scalene"

print(triangletypes(nums=[3, 4, 5]))