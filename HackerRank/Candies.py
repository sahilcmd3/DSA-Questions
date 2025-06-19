"""Alice is a kindergarten teacher. She wants to give some candies to the children in her class.  All the
children sit in a line and each of them has a rating score according to his or her performance in the class.
Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with
the higher rating must get more candies. Alice wants to minimize the total number of candies she must buy.
"""


def candies(n, arr):
    candie = [1] * n

    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            candie[i] = candie[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            candie[i] = max(candie[i], candie[i + 1] + 1)

    return sum(candie)


if __name__ == "__main__":
    print(candies(n=3, arr=[1, 2, 2]))
