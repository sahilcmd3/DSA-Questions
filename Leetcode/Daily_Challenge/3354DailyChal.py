# Make Array Elements Equal to Zero

"""You are given an integer array nums.
Start by selecting a starting position curr such that nums[curr] == 0, and choose a movement direction of either left or right.

After that, you repeat the following process:

    If curr is out of the range [0, n - 1], this process ends.
    If nums[curr] == 0, move in the current direction by incrementing curr if you are moving right, or decrementing curr if you are moving left.
    Else if nums[curr] > 0:
        Decrement nums[curr] by 1.
        Reverse your movement direction (left becomes right and vice versa).
        Take a step in your new direction.

A selection of the initial position curr and movement direction is considered valid if every element in nums becomes 0 by the end of the process.
Return the number of possible valid selections."""


class Solution:
    def countValidSelections(self, nums):
        n = len(nums)
        count = 0
        left = [0] * n
        right = [0] * n
        
        for i in range(1, n):
            left[i] = left[i - 1] + nums[i - 1]
            right[n - i - 1] = right[n - i] + nums[n - i]
            
        for i in range(n):
            if nums[i] != 0:
                continue
            if left[i] == right[i]:
                count += 2
            elif abs(left[i] - right[i]) == 1:
                count += 1
        
        return count


if __name__ == "__main__":
    obj = Solution()
    print(obj.countValidSelections(nums=[1, 0, 2, 0, 3]))
