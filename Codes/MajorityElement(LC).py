#LEETCODE

"""Given an array nums of size n, return the majority element.
The majority element is the element that appears more than [n / 2] times. You may assume that the majority element
always exists in the array."""

#Time complexity : O(n^2)
def majority_element(nums):
    n = len(nums)
    for i in set(nums):
        if nums.count(i) > n // 2:
            return i
    return None

nums = [2, 2, 1, 1, 1, 2, 2]
n = len(nums)
ans = majority_element(nums)
print(ans)


#Boyer-Moore Voting Algorithm
"""The Boyer-Moore voting algorithm is one of the popular optimal algorithms which is used to find the majority element
among the given elements that have more than N/ 2 occurrences. This works perfectly fine for finding the majority 
element which takes 2 traversals over the given elements, which works in O(N) time complexity and O(1) space complexity.

Algorithm:
Initialization: Start with a candidate set to None and a count set to 0.
First Pass - Candidate Selection: Iterate through the array. 
             For each element:
             If count is 0, set the candidate to the current element and set count to 1.
             If the current element is the same as the candidate, increment the count.
             If the current element is different from the candidate, decrement the count.
             By the end of this pass, the candidate will hold the majority element.
Second Pass - Candidate Verification:
              This step is optional if you are guaranteed that a majority element always exists.
              Iterate through the array again to verify that the selected candidate is indeed the majority 
              element by counting its occurrences.
              
#Solution
Time Complexity = O(n)
def majorityElement(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)
    return candidate"""