# Max Min


def maxMin(k, arr):
    arr.sort()
    i = 0
    ans = float("inf")

    while i + k - 1 < len(arr):
        ans = min(ans, arr[i + k - 1] - arr[i])
        i += 1

    return ans


if __name__ == "__main__":
    print(maxMin(arr=[1, 4, 7, 2], k=2))
