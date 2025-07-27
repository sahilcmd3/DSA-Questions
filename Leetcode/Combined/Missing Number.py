# LEETCODE 268

"""Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array."""


def missNum(nums):
    res=len(nums)
    
    for i in range(len(nums)):
        res += i -nums[i]
    
    return res

if __name__ == "__main__":
    print(missNum(nums=[3,0,1]))
