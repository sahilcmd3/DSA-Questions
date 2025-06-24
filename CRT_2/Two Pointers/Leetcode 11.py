# LEETCODE 11
# Time complexity: O(n)
def maxArea(height):
    max_area = 0
    left = 0  # area is directly proportional to length
    right = len(height) - 1

    while left < right:
        # length = right - left  &&   height = min(left, right) and then use max to get max area
        max_area = max(max_area, (right - left) * min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


print(maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
