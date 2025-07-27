def twoStacks(maxSum, a, b):
    i = j = total = count = 0

    # Take from stack a as long as we don't exceed maxSum
    while i < len(a) and total + a[i] <= maxSum:
        total += a[i]
        i += 1
    count = i

    # Now try to take from stack b, and backtrack from a if needed
    while j < len(b):
        total += b[j]
        j += 1

        while total > maxSum and i > 0:
            i -= 1
            total -= a[i]

        if total <= maxSum:
            count = max(count, i + j)

    return count


if __name__ == "__main__":
    print(twoStacks(maxSum=4, a=[1, 2, 3, 4, 5], b=[6, 7, 8, 9]))
