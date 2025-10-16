# Maximum Nesting Depth of the Parentheses

"""Given a valid parentheses string s, return the nesting depth of s. The nesting depth is the maximum number of nested parentheses."""


# Time Complexity: O(n)
class Solution:
    def maxDepth(self, s):
        count = 0
        max_num = 0

        for i in s:
            if i == "(":
                count += 1
                if max_num <= count:
                    max_num = count
            if i == ")":
                count -= 1

        return max_num


if __name__ == "__main__":
    obj = Solution()
    print(obj.maxDepth(s="(1+(2*3)+((8)/4))+1"))
