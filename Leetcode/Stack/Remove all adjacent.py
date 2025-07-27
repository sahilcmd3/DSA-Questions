# LEETCODE 1047


def removedupli(s):
    stack = []

    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


if __name__ == "__main__":
    print(removedupli(s="abbaca"))
