#LEETCODE (medium)

"""Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead."""


# Time Complexity: O(n)
def min_sub_arr(target, nums):
    min_len = float("inf") # Keeps track of the length of the smallest subarray. since we are looking for the minimum.
    left = 0 # Starting of sliding window
    cur_sum = 0 # Current sum of the sub array within the sliding window

    for right in range(len(nums)): # Moving the right pointer
        cur_sum += nums[right] # To expand the current window.

        while cur_sum >= target: # When cur_sum becomes greater than or equal to target,
            # it checks if the current window's length is smaller than min_len and updates min_len
            if right - left + 1 < min_len:
                min_len = right - left + 1
            cur_sum -= nums[left] # To find min sub array window is decreased and then checked again
            left += 1

    return min_len if min_len != float("inf") else 0


ans = min_sub_arr(target=7, nums=[2, 3, 1, 2, 4, 3])
print(ans)