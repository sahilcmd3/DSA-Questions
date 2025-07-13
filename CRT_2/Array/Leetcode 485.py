# Given a binary array nums, return the maximum number of consecutive 1's in the array.


# Time complexity: O(n)
def maxCon(nums):
    counter1 = 0
    counter = 0

    for i in range(len(nums)):
        if nums[i] == 0:
            counter = 0
        else:
            counter += 1
            counter1 = max(counter1, counter)

    return counter1


print(maxCon(nums=[1, 1, 0, 1, 1, 1]))
