# Minimum Number of Increments on Subarrays to Form a Target Array (Hard)

"""You are given an integer array target. You have an integer array initial of the same size as target with all elements initially zeros.
In one operation you can choose any subarray from initial and increment each value by one.
Return the minimum number of operations to form a target array from initial.

The test cases are generated so that the answer fits in a 32-bit integer."""


# Time Complexity: O(n)
class Solution:
    def minNumberOps(self, target: list[int]) -> int:
        res = prev = 0

        for x in target:
            if x > prev:
                res += x - prev
            prev = x

        return res


if __name__ == "__main__":
    obj = Solution()
    print(obj.minNumberOps(target=[3, 1, 5, 4, 2]))
