def largestRectangle(h):
    h.append(0)  # Sentinel to flush the stack at the end
    stack = []
    max_area = 0

    for i, height in enumerate(h):
        start = i
        while stack and stack[-1][1] > height:
            index, hgt = stack.pop()
            max_area = max(max_area, hgt * (i - index))
            start = index
        stack.append((start, height))

    return max_area


if __name__ == "__main__":
    print(largestRectangle(h=[3, 2, 3]))
