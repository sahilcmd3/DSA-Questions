def simpletexteditor(operations):
    text = []
    history = []
    output = []

    for op in operations:
        parts = op.split()
        if parts[0] == "1":
            history.append("".join(text))
            text.extend(parts[1])
        elif parts[0] == "2":
            history.append("".join(text))
            k = int(parts[1])
            text = text[:-k]
        elif parts[0] == "3":
            k = int(parts[1])
            output.append(text[k - 1])
        elif parts[0] == "4":
            text = list(history.pop())

    return output


if __name__ == "__main__":
    print(
        simpletexteditor(
            operations=["1 abc", "3 3", "2 3", "1 xy", "3 2", "4", "4", "3 1"]
        )
    )



"""# HackerRank Simple Text Editor - Full implementation

if __name__ == '__main__':
    q = int(input())
    text = []
    history = []

    for _ in range(q):
        parts = input().split()
        command = parts[0]

        if command == '1':
            # Save current state and append new string
            history.append(text.copy())
            text.extend(parts[1])
        elif command == '2':
            # Save current state and delete last k characters
            history.append(text.copy())
            k = int(parts[1])
            text = text[:-k]
        elif command == '3':
            # Print the k-th character (1-based)
            k = int(parts[1])
            print(text[k - 1])
        elif command == '4':
            # Undo: revert to last saved state
            text = history.pop()
"""
