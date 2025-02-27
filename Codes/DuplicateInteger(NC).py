# NEETCODE

"""Duplicate Integer
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false."""

# brute force solution
# time complexity= O(n^2)
# space complexity= O(n)
def check_duplicacy(arr):
    for i in range(0, len(arr)):  #traversing loop
        for j in range(i + 1, len(arr)):  #another traversing loop starting with i+1 index for comparison
            if arr[i] == arr[j]:
                return True
    return False


arr = [1, 2, 3, 3]
a = check_duplicacy(arr)
print(a)


# hash set solution
# hash is a key value pair here the value is a set and add values to the set
# sets do not contain duplicate values
#time complexity= O(n)
#space complexity= O(n)
class Solution:
    def hasduplicate(self, nums):
        seen = set()  #hash
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False