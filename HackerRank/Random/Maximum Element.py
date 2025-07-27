def getMax(operations):
    stack = []
    max_stack = []
    result = []

    for op in operations:
        parts = op.split()
        if parts[0] == "1":
            val = int(parts[1])
            stack.append(val)
            if not max_stack or val >= max_stack[-1]:
                max_stack.append(val)
        elif parts[0] == "2":
            remove = stack.pop()
            if remove == max_stack[-1]:
                max_stack.pop()
        elif parts[0] == "3":
            result.append(max_stack[-1])

    return result


if __name__ == "__main__":
    print(
        getMax(
            operations=["1 97", "2", "1 20", "2", "1 26", "1 20", "2", "3", "1 91", "3"]
        )
    )
