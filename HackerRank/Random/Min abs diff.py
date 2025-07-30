def minimumAbsoluteDifference(arr):
    arr.sort()
    a = arr[0] - arr[1]
    b = float("-inf")
    n = len(arr)
    for i in range(2, n):
        b = max(b, arr[i - 2] - a - arr[i])
        a = arr[i - 2] - a - arr[i]
    return abs(b)
