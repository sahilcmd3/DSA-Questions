#LEETCODE

"""Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the
characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of
"abcde" while "aec" is not)."""


#Time Complexity: O(n)
#Space Complexity: O(1)
def is_subsequence(s, t):
    sp = 0
    tp = 0

    while sp < len(s) and tp < len(t):
        if s[sp] == t[tp]:
            sp += 1
        tp += 1

    return sp == len(s)


ans = is_subsequence(s="abc", t="ahbgdc")
print(ans)