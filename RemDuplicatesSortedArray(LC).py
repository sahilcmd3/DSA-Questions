#LEETCODE

"""Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place algo such that each
unique element appears only once. The relative order of the elements should be kept the same.
Then return the number of unique elements in nums. Consider the number of unique elements of nums to be k,
to get accepted, you need to do the following things:
    Change the array nums such that the first k elements of nums contain the unique elements in the order
    they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    Return k

In Place algo operates directly on the input data structure"""

#Time Complexity = O(n^2)
"""def removeDuplicates(nums):
    i=0
    while i<len(nums)-1:
        if nums[i]==nums[i+1]:
            nums.pop(i+1) #pop here increased the time
        else:
            i+=1
    return len(nums), nums

nums=[1,1,2]
a=removeDuplicates(nums)
print(a)"""


#Time Complexity = O(n)
def removeDuplicates(nums):
    k = 1  #write index
    for i in range(1, len(nums)):  #i is read index
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k, nums[:k]  #array slicing


nums = [1, 1, 2]
a = removeDuplicates(nums)
print(a)