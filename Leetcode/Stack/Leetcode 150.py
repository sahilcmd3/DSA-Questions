# Evaluate Reverse Polish Notation

"""You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

# Time Complexity: O(n)
class Solution:
    def evalRPN(self, tokens):
        st = []

        for c in tokens:
            if c == "+":
                st.append(st.pop() + st.pop())
            elif c == "-":
                second, first = st.pop(), st.pop()
                st.append(first - second)
            elif c == "*":
                st.append(st.pop() * st.pop())
            elif c == "/":
                second, first = st.pop(), st.pop()
                st.append(int(first / second))
            else:
                st.append(int(c))

        return st[0]


if __name__ == "__main__":
    obj = Solution()
    print(obj.evalRPN(tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
