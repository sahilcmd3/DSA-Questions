# LEETCODE 229

# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.# 

"""BOYER-MOORE MAJORITY VOTE ALGO
The algorithm above is known as Boyer-Moore Majority Vote Algorithm.
The Boyer-Moore Majority Vote Algorithm is an efficient algorithm used to find the majority element (an element that appears more than 
half of the time) in a given array. This algorithm operates in linear time and requires O(1) additional space.

Here are the basic steps of the Boyer-Moore Majority Vote Algorithm:
    - Candidate Element Selection: Choose the first element of the array as the candidate element and initialize a counter.
    - Element Counting: Traverse through the array. If the current element matches the candidate element, increment the counter. If they 
        don't match, decrement the counter.
    - Check Counter: If the counter becomes zero, choose the current element as the new candidate element and reset the counter to one.
    - Final Candidate Verification: After these steps, verify if the selected candidate is indeed the majority element.

By following these steps, the algorithm efficiently identifies the most frequently occurring element, if one exists, in linear time O(n) in 
the worst case. This efficiency is achieved by carefully selecting candidate elements and comparing them against other elements."""


# Time Complexity: O(n)
# Space Complexity: O(1)
def majorityEle(nums):
    # Initialize majority1, majority2, count1, and count2 to track the majority elements and their counts
    majority1 = 0
    majority2 = 0
    count1 = 0
    count2 = 0

    # Iterate through the input list nums to find the two majority elements
    for num in nums:
        if num == majority1:
            count1 += 1
        elif num == majority2:
            count2 += 1
        elif count1 == 0:
            majority1 = num
            count1 += 1
        elif count2 == 0:
            majority2 = num
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1

    # Verifing that majority1 and majority2 appear more than n/3 times.
    count1 = 0
    count2 = 0

    # Iterate through nums again to verify the counts of the two majority elements.
    for num in nums:
        if num == majority1:
            count1 += 1
        elif num == majority2:
            count2 += 1

    result = []
    if count1 > len(nums) // 3:
        result.append(majority1)
    elif count2 > len(nums) // 3:
        result.append(majority2)

    return result


if __name__ == "__main__":
    print(majorityEle(nums=[1,2]))
