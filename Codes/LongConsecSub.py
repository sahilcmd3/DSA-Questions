# LEETCODE (medium)

"""Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time."""


# Time complexity: O(n)
def long_cons(nums):
    num_set = set(nums)  # converts the nums to hash set changing the membership checks from O(n) to O(1)
    longest = 0

    for n in num_set:
        if n-1 not in num_set:  # This ensures we only start counting sequences at the smallest number in a sequence.
            # If n-1 exists, then n is part of an ongoing sequence and should be skipped.
            length = 1

            while n+length in num_set:  # If n is the start of a sequence, this loop extends the sequence by checking 
                # whether n + length exists in num_set.
                length += 1

            longest = max(longest, length)

    return longest


print(long_cons(nums=[100, 4, 200, 1, 3, 2]))