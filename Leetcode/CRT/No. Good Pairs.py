#LEETCODE

def gpairs(nums):
    pairs={}
    count=0

    for i in range(len(nums)):
        if nums[i] in pairs:
            count += pairs[nums[i]]

        pairs[nums[i]] = pairs.get(nums[i],0) + 1

    return count

ans=gpairs(nums=[1,2,3,1,1,3])
print(ans)