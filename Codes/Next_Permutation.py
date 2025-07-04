# STRIVER (LEETCODE)

"""A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3],
                                                                               [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order,
then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is
not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory."""


def nextper(nums):
    i = len(nums) - 1
    while i > 0 and nums[i - 1] >= nums[i]:  # Starts from the right and moves left to find the first decreasing element.
    # Example: For [1,2,3], 2 is the first decreasing element.
        i -= 1

    if i == 0:  # Handling Edge case
        nums.reverse()
        return

    j = len(nums) - 1  # Finds the smallest number greater than nums[i - 1] on the right side.
    while j >= i and nums[j] <= nums[i - 1]:
        j -= 1

    # Swapping
    nums[i - 1], nums[j] = nums[j], nums[i - 1]

    # Reversing the right portiom
    nums[i:] = reversed(nums[i:])

    return nums


print(nextper(nums=[1, 2, 3]))