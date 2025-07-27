# LEETCODE

"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type."""


# Time Complexity: O(n)
def isValid(s):
    st = []
    mapp = {")": "(", "}": "{", "]": "["}

    for char in s:
        if char in mapp.values():
            st.append(char)
        elif char in mapp.keys():
            if not st or mapp[char] != st.pop():
                return False

    return not st


print(isValid(s = "()[]{}"))
