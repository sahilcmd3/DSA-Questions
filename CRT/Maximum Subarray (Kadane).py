# Kadane' algorithm

"""Kadane's Algorithm is an efficient method used to solve the **Maximum Subarray Problem**, which involves finding
the contiguous subarray with the largest sum in a given array.

### **How It Works**
1. **Initialize two variables**:
   - `max_sum`: Stores the maximum sum found so far.
   - `current_sum`: Tracks the sum of the current subarray.

2. **Iterate through the array**:
   - At each step, decide whether to **extend the current subarray** or **start a new one**.
   - Update `max_sum` whenever `current_sum` exceeds it.

3. **Return `max_sum`**, which holds the largest sum of any contiguous subarray."""


# LEETCODE (medium)

"""Given an integer array nums, find the subarray with the largest sum, and return its sum."""


#Time Complexity:O(n)
def kadane(arr):
    max_sum = float('-inf')  # Initialize to negative infinity
    current_sum = 0

    for num in arr:
        current_sum = max(num, current_sum + num)  # Extend or start new subarray
        max_sum = max(max_sum, current_sum)  # Update max sum

    return max_sum


print(kadane(arr= [-2, 1, -3, 4, -1, 2, 1, -5, 4]))