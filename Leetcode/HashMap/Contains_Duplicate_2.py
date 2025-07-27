# LEETCODE

"""Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k."""


# Time Complexity: O(n)
def near_dup(nums, k):
    visited = {}

    # built-in function that adds a counter to an iterable and returns it as an enumerate object.
    for i, val in enumerate(nums):
        # This is especially useful when you need both the index and the value while looping through a list, tuple, or other iterable.
        if val in visited and i - visited[val] <= k:
            return True
        else:
            visited[val] = i

    return False


print(near_dup(nums=[1, 2, 3, 1], k=3))
