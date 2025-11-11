# Ones and Zeroes

"""You are given an array of binary strings strs and two integers m and n.
Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.
A set x is a subset of a set y if all elements of x are also elements of y."""

from typing import List


class Solution:
    def findmaxform(self, strs: List[str], m: int, n: int) -> int:
        dp = {(0, 0): 0}

        for s in strs:
            zeros = s.count("0")
            ones = s.count("1")

            # iterate over a snapshot so we can safely modify dp
            for (z, o), cnt in list(dp.items()):
                nz, no = z + zeros, o + ones
                if nz <= m and no <= n:
                    dp[(nz, no)] = max(dp.get((nz, no), 0), cnt + 1)

        return max(dp.values())


if __name__ == "__main__":
    obj = Solution()
    print(obj.findmaxform(strs=["10", "0001", "111001", "1", "0"], m=5, n=3))
