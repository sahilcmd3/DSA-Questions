# First negative in every window of size k (GFG)

from collections import deque

def firstNeg(arr, k):
    n = len(arr)
    result = []
    dq = deque()

    for i in range(n):
        # Remove indices out of the current window
        if dq and dq[0] <= i - k:
            dq.popleft()

        # If current element is negative, add its index
        if arr[i] < 0:
            dq.append(i)

        # Append result once the first window is complete
        if i >= k - 1:
            result.append(arr[dq[0]] if dq else 0)

    return result


if __name__ == "__main__":
    print(firstNeg(arr=[-8, 2, 3, -6, 10], k=2))
