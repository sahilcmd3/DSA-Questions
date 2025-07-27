#LEETCODE

def ads(n):  #approach O(log n)
    sum = 0
    while n:
        sum = (n % 10) - sum
        n //= 10
    return sum


ans = ads(n=521)
print(ans)

"""Another approach
convert int to string
find length of the string
find odd, even sum
a-b/b-a depending on length"""
