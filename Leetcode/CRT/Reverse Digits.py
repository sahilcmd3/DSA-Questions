#LEETCODE

def revedigits(n):
    reverse_str = ""
    while n > 0:
        reverse_str += str(n % 10)
        n //= 10
    return int(reverse_str)

ans = revedigits(n=122)
print(ans)