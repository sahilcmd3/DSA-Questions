#LEETCODE

def palindrome(n):
    s = str(n)
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True

ans = palindrome(n = 121)
print(ans)