# LEETCODE

"""You are given a string s consisting of lowercase English letters.

Your task is to find the maximum difference diff = freq(a1) - freq(a2) between the frequency of characters a1 and a2 in the string such that:

a1 has an odd frequency in the string.
a2 has an even frequency in the string.
Return this maximum difference."""


from collections import Counter


def maxDiff(s):
    freq = Counter(s)
    odd = 0
    even = len(s)

    for count in freq.values():
        if count % 2 == 1:
            odd = max(odd, count)
        elif count != 0:
            even = min(even, count)

    return odd - even


print(maxDiff(s="aaaaabbc"))
