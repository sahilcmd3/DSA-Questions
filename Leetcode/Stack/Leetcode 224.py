# Basic Calculator

"""Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
"""


# Time Complexity: O(n)
class Solution:
    def calculate(self, s):
        ans = 0
        num = 0
        sign = 1
        stack = [sign]

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "(":
                stack.append(sign)
            elif c == ")":
                stack.pop()
            elif c == "+" or c == "-":
                ans += sign * num
                sign = (1 if c == "+" else -1) * stack[-1]
                num = 0

        return ans + sign * num


if __name__ == "__main__":
    obj = Solution()
    print(obj.calculate(s="1 + 1"))
