# LEETCODE 1944


def canSee(heights):
    n = len(heights)
    result = [0] * n
    stack = []

    for i in range(n - 1, -1, -1):
        count = 0
        while stack and heights[i] > stack[-1]:
            stack.pop()
            count += 1
        if stack:
            count += 1

        result[i] = count
        stack.append(heights[i])

    return result


if __name__ == "__main__":
    print(canSee(heights=[10, 6, 8, 5, 11, 9]))
