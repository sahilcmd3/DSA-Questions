# LEETCODE 152

"""Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer."""


# Time complexity: O(n)
class Solution:
    def maxProduct(self, nums):
        res = max(nums)
        curr_max = curr_min = 1

        for n in nums:
            temp = curr_max * n
            curr_max = max(temp, curr_min * n, n)
            curr_min = min(temp, curr_min * n, n)

            res = max(res, curr_max)
        
        return res


if __name__ == "__main__":
    obj = Solution()
    print(obj.maxProduct(nums=[2,3,-2,4]))
