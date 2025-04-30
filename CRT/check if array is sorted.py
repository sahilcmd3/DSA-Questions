# GFG

"""Check if array is sorted"""


def check(arr):
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True


ans = check(arr=[1, 2, 18, 6])
print(ans)