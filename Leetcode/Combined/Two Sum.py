# LEETCODE 1

"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order."""


def twoSum(nums, target):
    num_map = {}

    for i, num in enumerate(nums):
        comple = target - num

        if comple in num_map:
            return [num_map[comple], i]
        num_map[num] = i

    return False


if __name__ == "__main__":
    print(twoSum(nums=[2, 7, 11, 15], target=9))
