#HACKER RANK

def sherlock(arr):
    left = 0
    right = sum(arr)
    for i in range(len(arr)):
        if i != 0:
            left += arr[i - 1]
        right -= arr[i]
        if left == right:
            return 'YES'
    return 'NO'

a=sherlock(arr=[5,6,8,11])
print(a)