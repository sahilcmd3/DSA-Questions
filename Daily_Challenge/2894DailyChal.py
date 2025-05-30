# LEETCODE

"""You are given positive integers n and m.

Define two integers as follows:

num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
Return the integer num1 - num2."""


# Time Complexity: O(1)
def differenceOfSums(n, m):
    total_sum = n * (n + 1) // 2
    divisible_count = n // m
    divisible_sum = m * divisible_count * (divisible_count + 1) // 2

    return total_sum - 2 * divisible_sum


print(differenceOfSums(n=10, m=3))