#LEETCODE (medium)

"""Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and
j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets."""


# Time Complexity: O(n^2)
def threeSum(nums):
    res=[] # Empty list to store triplets whose sum is zero
    nums.sort()

    for i in range(len(nums)):
        if i>0 and nums[i]==nums[i-1]: # Check if the current element is a duplicate of the previous element and
            # skip it if it is
            continue

        j=i+1 # Points to next element to the current element i
        k=len(nums)-1 # Points to the end of the array

        while j<k:
            total = nums[i]+nums[j]+nums[k]

            if total>0:
                k-=1
            elif total<0:
                j+=1
            else:
                res.append([nums[i],nums[j],nums[k]])
                j+=1

                while nums[j]==nums[j-1] and j<k: # Increment the j pointer to skip any duplicate elements
                    j+=1

    return res

ans=threeSum(nums=[-1,0,1,2,-1,-4])
print(ans)