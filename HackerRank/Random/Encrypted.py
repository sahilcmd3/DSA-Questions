# HackerRank -> Encrypted

# Time Complexity: O(n^2)
def encryption(s):
    s = s.replace(" ", "")
    l = len(s)

    sqrt = 0
    while (sqrt + 1) * (sqrt + 1) <= l:
        sqrt += 1

    rows = sqrt
    columns = sqrt if sqrt * sqrt >= l else sqrt + 1

    if rows * columns < l:
        rows += 1

    encrypted = []
    for c in range(columns):
        word = ""
        for r in range(rows):
            idx = r * columns + c
            if idx < l:
                word += s[idx]

        encrypted.append(word)

    return " ".join(encrypted)


if __name__ == "__main__":
    print(encryption(s="chillout"))
