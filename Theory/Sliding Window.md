### Definition:
The sliding window technique is an algorithmic approach used in a computer science and signal processing. It involves
selecting a fixed-size subset or "window" from a larger dataset and moving this window through the dataset in a step-
wise fashion.

This window slides over the data, typically one a time and performs some operations on the elements within the window at
each step.

### Types:
There are two main types of sliding windows:
    - Fixed-Size Sliding Window: The window size remains constant throughout the process. This is often used to
      find a specific sum, maximum, or minimum within subarrays or substrings of a fixed size.
    - Variable-Size Sliding Window: The window size changes dynamically based on the problem's constraints.
      This is often used to find the longest or smallest subarrays/substrings that meet specific conditions.

### Steps to Use Sliding Window Technique
 - Fixed Size:
   * Define the window size k.
   * Compute the result for the first window (the first k elements).
   * Slide the window one element at a time, efficiently updating the result by adding the new element and
     removing the first element from the previous window.

 - Variable Size:
   * Use two pointers (start and end) to represent the window.
   * Increase the end pointer until the condition is satisfied.
   * Once the condition is not satisfied, shrink the window by moving the start pointer.
   * Continue until the desired result is achieved or the array/string is fully traversed.

### Example
Maximum Sum of Subarray of Size k
Let's say we are given an array and need to find the maximum sum of subarrays of size k.
Problem:
Input: arr = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4 Output: 39

Sliding Window Solution:
 - Compute the sum of the first k elements (window_sum).
 - For the first window [1, 4, 2, 10], window_sum = 1 + 4 + 2 + 10 = 17.
 - Slide the window one element at a time:
 - Remove the first element from the previous window and add the next element in the array.
 - For the next window [4, 2, 10, 23], update window_sum = 17 - 1 + 23 = 39.
 - Keep track of the maximum sum seen so far.

Python Code:

def max_sum(arr, k):
    n = len(arr)
    if n < k:
        return "Invalid: Array size is less than window size."

    # Calculate initial window sum
    window_sum = sum(arr[:k])
    max_sum = window_sum

    # Slide the window
    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum

arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(max_sum(arr, k))  # Output: 39

This approach reduces the time complexity to O(n) compared to the naive solution using nested loops, which has
a time complexity of O(kn)*.

### The Sliding Window Technique is incredibly versatile and can also be used to solve other problems like:
    - Finding the longest substring without repeating characters.
    - Finding the smallest subarray with a sum greater than a given value.
    - Count distinct elements in every window of size k.