# Minimum Operations to Convert All Elements to Zero

"""You are given an array nums of size n, consisting of non-negative integers. Your task is to apply some (possibly zero)
operations on the array so that all elements become 0.

In one operation, you can select a subarray [i, j] (where 0 <= i <= j < n) and set all occurrences of the minimum non-negative
integer in that subarray to 0.

Return the minimum number of operations required to make all elements in the array 0."""


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        st = [-1]
        op = 0
        for x in nums:
            while x < st[-1]:
                st.pop()
            if x > st[-1]:
                op += x > 0
                st.append(x)
        return op


if __name__ == "__main__":
    obj = Solution()
    print(obj.minOperations(nums=[0, 2]))
