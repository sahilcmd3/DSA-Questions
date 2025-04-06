#LEETCODE

def missing_num(nums):
    res=len(nums)

    for i in range(len(nums)):
        res += i-nums[i]

    return res

ans=(missing_num(nums=[3,0,1]))
print(ans)