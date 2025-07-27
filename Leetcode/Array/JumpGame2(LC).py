#LEETCODE (medium)

"""You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index i. In other words,
if you are at nums[i], you can jump to any nums[i + j] where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that
you can reach nums[n - 1].

Explanation: Jump Game II is a problem on LeetCode where you're given an array of integers called nums.
The objective is to find the minimum number of jumps needed to reach the last index of the array.
Here's the problem statement in a nutshell:
    You start at the first index of the array (nums[0]).
    Each element in the array (nums[i]) represents the maximum number of steps you can jump forward from that index.
    You need to find the minimum number of jumps to reach the last index of the array."""

#Greedy approach Time complexity: O(n)
def jump(nums):
    jumps = 0 #number of jumps = 0
    cur_end = 0 #the end of the range that current jump can reach
    cur_farthest = 0 #The farthest point that can be reached from the current range

    for i in range(len(nums) - 1):
        cur_farthest = max(cur_farthest, i + nums[i])
        if i == cur_end:
            jumps += 1
            cur_end = cur_farthest
            if cur_end >= len(nums) - 1:
                break
    return jumps


nums = [2, 3, 1, 1, 4]
ans = jump(nums)
print(ans)

"""Walk through:
Let's walk through the example nums = [2, 3, 1, 1, 4]:
At the start, jumps = 0, cur_end = 0, and cur_farthest = 0.

First iteration (i = 0):
cur_farthest = max(0, 0 + 2) = 2.
Since i == cur_end (0 == 0):
jumps += 1 → jumps = 1.
cur_end = cur_farthest → cur_end = 2.

Second iteration (i = 1):
cur_farthest = max(2, 1 + 3) = 4.
Since i == cur_end is false (1 != 2), continue to the next iteration.

Third iteration (i = 2):
cur_farthest = max(4, 2 + 1) = 4.
Since i == cur_end (2 == 2):
jumps += 1 → jumps = 2.
cur_end = cur_farthest → cur_end = 4.
Since cur_end >= n - 1 (4 >= 4), break out of the loop."""