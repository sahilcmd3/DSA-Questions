#LEETCODE (Hard)

#Trapping Rain water

"""Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much
water it can trap after raining."""

#Time Complexity: O(n)
#Space Complexity: O(1)
def trap(height):

    left = 0 # Initialize two pointers left and right at the beginning and end of the height list respectively
    right = len(height) - 1
    left_max = height[left] # Initialize variables left_max and right_max to store the maximum height encountered from
    right_max = height[right] # the left and right sides respectively.
    water = 0 # Initialize variable water to keep track of the total trapped water.

    while left < right: # Continue looping while left pointer is less than right pointer, indicating there are still bars to process.
        """ Check which side to move:
                Compare left_max and right_max heights.
                If left_max is less than right_max, move the left pointer to the right and update left_max.
                Otherwise, move the right pointer to the left and update right_max. """
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
            # Calculate the water trapped at the current position based on the difference between the maximum height and
            # the current height.
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]

    return water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
ans = trap(height)
print(ans)