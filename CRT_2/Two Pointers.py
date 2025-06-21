# LEETCODE 977
"""Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order."""

# Two pointer approach
# Time Complexity: O(n)
def sortedSquares(nums):
    n = len(nums)
    answer = [0] * n

    left = 0
    right = n - 1

    for i in range(n - 1, -1, -1):
        if abs(nums[left]) > abs(nums[right]):
            answer[i] = nums[left] ** 2
            left += 1
        else:
            answer[i] = nums[right] ** 2
            right -= 1

    return answer



# LEETCODE 283
"""Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array."""

# Two pointer approach
# Time complexity: O(n)
def moveZereos(nums):
    left = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
            
    return nums



# LEETCODE 167
# Time complexity: O(n)
def twoSumTwo(numbers, target):
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total > target:
            left -= 1
        else:
            right += 1
            


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


if __name__ == "__main__":
    #print(sortedSquares(nums=[-4, -1, 0, 3, 10]))
    #print(moveZereos(nums = [0,1,0,3,12]))
    #print(twoSumTwo(numbers=[2,7,11,15], target = 9))
    print(maxArea(height = [1,8,6,2,5,4,8,3,7]))
