#LEETCODE (medium)

"""You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.

Explanation: The question states "each element in the array represents your maximum jump length at that position."
It means if we are at a position k and nums[k] = 4, then it means we can jump forward a maximum of 4 steps from
this position. It's our choice to jump 1,2,3 or 4 positions, but not more than 4.

    For example:
    In this test case [2,3,1,4]
    nums[0] = 2
    It means we can jump either 1 or 2 steps
    At the end, we have to reach the last index"""

#GREEDY Approach Time complexity: O(n)
def can_jump(nums):
    max_reachable=0
    for i,jump in enumerate(nums): # This line loops through the list nums using the enumerate function,
        # which provides both the index (i) and the value (jump) of each element in the list.
        if i>max_reachable:
            return False
        max_reachable=max(max_reachable,i+jump) #This line updates max_reachable to be the maximum of its
        # current value and the sum of the current index i and the jump value jump.
        # This represents the furthest index that can be reached from the current position.
    return True

nums = [2, 3, 1, 1, 4]
ans=can_jump(nums)
print(ans)


#Another greedy approach better
"""def canJump(nums):
        gas=0 #steps
        for n in nums:
            if gas<0:
                return False
            elif n>gas: #if next step has better jump capacity move to it and exchange value
                gas=n
            gas -=1 #decrease by one after moving each step
        return True"""