# The Two Sneaky Numbers of Digitville

"""In the town of Digitville, there was a list of numbers called nums containing integers from 0 to n - 1. Each number was supposed to
appear exactly once in the list, however, two mischievous numbers sneaked in an additional time, making the list longer than usual.

As the town detective, your task is to find these two sneaky numbers. Return an array of size two containing the two numbers (in any order),
so peace can return to Digitville."""


class Solution:
    # Time Complexity: O(n)
    def sneaky(self, nums: list[int]) -> list[int]:
        n = len(nums)
        seen = [False] * n
        res: list[int] = []

        for i in nums:
            if seen[i]:
                res.append(i)
            else:
                seen[i] = True

        return res

    # XOR Solution
    # Time Complexity: O(n)
    def sneaky_XOR(self, a: list[int]) -> list[int]:
        # Calculate n: the expected range is [0, n-1], but array has n+2 elements
        # This means there are 2 extra/different numbers in the array
        n = len(a) - 2

        # Step 1: Find XOR of the two different numbers
        xor = 0

        # XOR all elements in the input array
        for num in a:
            xor ^= num

        # XOR with all expected numbers [0, n-1]
        # After this, 'xor' contains (p ^ q) where p and q are the two different numbers
        # This works because XORing a number with itself gives 0
        for i in range(n):
            xor ^= i

        # Step 2: Find a bit position where p and q differ
        # xor & -xor isolates the rightmost set bit
        # This bit is 1 in exactly one of p or q, and 0 in the other
        diffBit = xor & -xor

        # Step 3: Partition all numbers into two groups based on the diffBit
        # Group 1 (p): numbers with diffBit = 0
        # Group 2 (q): numbers with diffBit = 1
        p = q = 0

        # Partition the input array elements
        for num in a:
            if num & diffBit == 0:
                p ^= num  # XOR all numbers with diffBit = 0
            else:
                q ^= num  # XOR all numbers with diffBit = 1

        # Partition the expected range [0, n-1]
        for i in range(n):
            if i & diffBit == 0:
                p ^= i  # XOR all expected numbers with diffBit = 0
            else:
                q ^= i  # XOR all expected numbers with diffBit = 1

        # After partitioning and XORing, p and q contain the two different numbers
        # This works because all matching numbers cancel out (a ^ a = 0)
        return [p, q]

    """Algorithm Summary:
    This solves the problem of finding two numbers that differ between an array and the expected range [0, n-1]. It uses XOR properties:
    - `a ^ a = 0` (self-cancellation)
    - `a ^ 0 = a` (identity)
    - XOR is commutative and associative

    The trick is to use a differentiating bit to separate the two unknown numbers into different groups, so they can be found independently."""


if __name__ == "__main__":
    obj = Solution()
    print(obj.sneaky(nums=[0, 1, 1, 0]))
    print(obj.sneaky_XOR(a=[0, 1, 1, 0]))
