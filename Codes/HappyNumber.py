# LEETCODE

"""Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum of the squares of its digits.
    Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
    Those numbers for which this process ends in 1 are happy.

Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1"""


# Universal function
def logic(n):  
    output = 0

    while n:
        digit = n % 10  # extract last digit of n
        output += digit**2  # square n and store
        n = n // 10  # remove last element & repeat till n=0

    return output


# Time complexity: O(log n)
# 100% beat
# Floyd Cycle approach (turtle = slow & hare = fast), cycle detection algorithm
# Two pointer approach (slow and fast (2 * slow)) 
# Little less memory required
def happy_num(n):
    slow = logic(n)
    fast = logic(logic(n))  # is set to the next number of the next number of n

    while slow != fast:
        if fast == 1:
            return True

        slow = logic(slow)  # Slow moved to next number
        fast = logic(logic(fast))  # Fast moved to next to next

    return slow == 1


# Hash set approach
# Time complexity: O(log n)
# 100 %
# Little more memory required
def happy_num(n):
    visited=set()  # To keep track of numbers for cycle repeation

    while n not in visited:  
        visited.add(n)
        n=logic(n)  # Continously generate next num
        if n==1:
            return True
    
    # If cycle appears
    return False  

print(happy_num(n=19))