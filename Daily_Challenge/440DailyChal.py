# LEETCODE (Hard)

"""Given two integers n and k, return the kth lexicographically smallest integer in the range [1, n].

Example 1:
Input: n = 13, k = 2
Output: 10
Explanation: The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so the second smallest number is 10.

Example 2:
Input: n = 1, k = 1
Output: 1"""


# Time Complexity: O(log(n) * log(k)) due to the logarithmic depth of the tree traversal
class Solution:
    def findkth(self, n, k):
        current = 1
        k -= 1

        while k > 0:
            count = self.countSteps(n, current, current + 1)
            if count <= k:
                current += 1
                k -= count
            else:
                current *= 10
                k -= 1

        return current

    def countSteps(self, n, curr, next):
        steps = 0

        while curr <= n:
            steps += min(n + 1, next) - curr
            curr *= 10
            next *= 10

        return steps


obj = Solution()
print(obj.findkth(n=13, k=2))
