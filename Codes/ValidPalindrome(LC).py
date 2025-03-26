#LEETCODE

"""A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all
non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise."""

#Time Complexity: O(N)
def is_palindrome(s):

    s=''.join(c.lower() for c in s if c.isalnum())

    left=0
    right=len(s)-1

    while left<right:
        if s[left]!=s[right]:
            return False

        left+=1
        right-=1

    return True


ans = is_palindrome(s="A man, a plan, a canal: Panama")
print(ans)