"""Palindromes are strings that read the same from the left or right, for example madam or 0110.

You will be given a string representation of a number and a maximum number of changes you can make. Alter the string,
one digit at a time, to create the string representation of the largest number possible given the limit to the number of changes.
The length of the string may not be altered, so you must consider 0's left of all higher digits in your tests. For example 0110 is valid,
0011 is not.

Given a string representing the starting number, and a maximum number of changes allowed, create the largest palindromic string of digits
possible or the string '-1' if it is not possible to create a palindrome under the contstraints.
"""


def highestValuePalindrome(s, n, k):
    s = list(s)
    changes = [False] * n

    # Making a palindrome
    left = 0
    right = n - 1

    while left < right:
        if s[left] != s[right]:
            s[left] = s[right] = max(s[left], s[right])
            changes[left] = changes[right] = True
            k -= 1

        left += 1
        right -= 1

    if k < 0:
        return "-1"

    # Maximize the palindrome
    left = 0
    right = n - 1
    while left <= right:
        if left == right:  # Middle element in odd-length strings
            if k > 0:
                s[left] = "9"
        elif s[left] != "9":  # Trying to maximize both sides
            if changes[left] or changes[right]:  # Already changed once
                if k > 0:
                    s[left] = s[right] = "9"
                    k -= 1
            else:  # Not changed yet
                if k > 1:
                    s[left] = s[right] = "9"
                    k -= 2

        left += 1
        right -= 1

    return "".join(s)


if __name__ == "__main__":
    print(highestValuePalindrome(n=4, k=1, s="3943"))
