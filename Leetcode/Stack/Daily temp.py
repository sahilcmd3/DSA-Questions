# LEETCODE 739

def temp(temperatures):
    n = len(temperatures)
    answer = [0] * n
    stack = []  # stores indices

    for i in range(n - 1, -1, -1):
        while stack and temperatures[i] >= temperatures[stack[-1]]:
            stack.pop()
        if stack:
            answer[i] = stack[-1] - i
        stack.append(i)

    return answer


if __name__ == "__main__":
    print(temp(temperatures=[73, 74, 75, 71, 69, 72, 76, 73]))
