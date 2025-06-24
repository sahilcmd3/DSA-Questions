# LEETCODE 287

"""Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and using only constant extra space.
"""


def findDup(nums):
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return nums[i]


# extra set is used
# Time complexity: O(n)
# Space complexity: O(n)
def findDupli(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return num

        seen.add(num)

    return -1


# Floyd Cycle Detection
# Time complexity: O(n)
# Space Complexity: O(1)
def findDuplic(nums):
    slow = nums[0]
    fast = nums[0]
    
    while True:
        slow=nums[slow]
        fast=nums[nums[fast]]
        
        if slow==fast:
            break
    
    slow=nums[0]
    
    while slow != fast:
        slow=nums[slow]
        fast=nums[fast]
    
    return slow


if __name__ == "__main__":
    # print(findDup(nums=[1, 3, 4, 2, 2]))
    # print(findDupli(nums=[1, 3, 4, 2, 2]))
    print(findDuplic(nums=[1, 3, 4, 2, 2]))