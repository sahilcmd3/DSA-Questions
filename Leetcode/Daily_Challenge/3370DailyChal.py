# Smallest Number With All Set Bits

"""You are given a positive number n.
Return the smallest number x greater than or equal to n, such that the binary representation of x contains only set bits.
A set bit refers to a bit in the binary representation of a number that has a value of 1"""

"""These are numbers of the form 2^k - 1: 1, 3, 7, 15, 31, 63, etc.
In binary: 1, 11, 111, 1111, 11111, 111111, etc."""


class Solution:
    def smallestNumber(self, n: int) -> int:
        # Loop while n is NOT a number with all bits set to 1
        # Key insight: If n has all bits as 1 (like 111 in binary), then n+1 will be a power of 2 (like 1000 in binary).
        # So n & (n+1) will be 0 for numbers with all bits set to 1.
        # If n & (n+1) != 0, we need to keep setting more bits.
        while n & (n + 1):
            # OR operation with (n+1) helps turn on the bits that are 0
            # This gradually converts n to have all consecutive 1s from the rightmost bit up to the most significant bit
            n |= n + 1

        # Once all bits are 1s, return the result
        return n


if __name__ == "__main__":
    obj = Solution()
    # Example: n=5 (binary: 101)
    # Iteration 1: 5 & 6 = 101 & 110 = 100 (not 0, continue)
    #              5 | 6 = 101 | 110 = 111 = 7
    # Iteration 2: 7 & 8 = 111 & 1000 = 0 (exit loop)
    # Result: 7 (binary: 111)
    print(obj.smallestNumber(n=5))  # Output: 7
