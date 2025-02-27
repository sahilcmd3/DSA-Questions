#LEETCODE (medium)

"""Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each
unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages (not in python), you must instead have the
result be placed in the first part of the array nums. More formally, if there are k elements after
removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you
leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums. Do not allocate extra space for another array.
You must do this by modifying the input array in-place with O(1) extra memory."""


def rem_duplicates(nums):
    k = 2  #k is 2 because at most 2 places can be same so we start the first counter after 2 places
    for i in range(2, len(nums)):  #here the 2nd counter starts after 2nd place
        if nums[i] != nums[i - 2]:  #condition check
            nums[k] = nums[i]
            k += 1
    return k, nums


nums = [1, 1, 1, 2, 2, 3]
ans = rem_duplicates(nums)
print(ans)