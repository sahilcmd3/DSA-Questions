def isBalanced(s):
    stack = []
    bracket_map = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in bracket_map.values():  # opening brackets
            stack.append(char)
        elif char in bracket_map:  # closing brackets
            if not stack or stack[-1] != bracket_map[char]:
                return "NO"
            stack.pop()
        else:
            return "NO"  # invalid character (optional safety)

    return "YES" if not stack else "NO"


if __name__ == "__main__":
    print(isBalanced(s= "{[()]}"))