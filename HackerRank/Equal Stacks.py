# HackerRank Equal Stacks


def equalStacks(h1, h2, h3):
    # Convert each list into a stack of cumulative heights from top to base
    def stack_heights(heights):
        total = sum(heights)
        stack = [total]
        for h in heights:
            total -= h
            stack.append(total)
        return stack

    s1 = set(stack_heights(h1))
    s2 = set(stack_heights(h2))
    s3 = set(stack_heights(h3))

    # Find the highest common height
    common = s1 & s2 & s3
    return max(common) if common else 0


if __name__ == "__main__":
    print(equalStacks(h1=[1, 2, 1, 1], h2=[1, 1, 2], h3=[1, 1]))
