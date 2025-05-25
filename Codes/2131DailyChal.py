# LEETCODE (Medium)

"""You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element 
can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

Example 1:

Input: words = ["lc","cl","gg"]
Output: 6
Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
Note that "clgglc" is another longest palindrome that can be created."""


from collections import Counter


# Time complexity: O(n+26^2)
def longPalin(words):
    freq = Counter(words)
    pal = 0 
    hasDouble = False

    for key, val in freq.items():
        # For words with identical letters 
        if key[0] == key[1]:
            pal += val // 2 * 4  # Each pair contributes 4 characters to palindrome length
            if val & 1:  # If odd count remains, one can go in center
                hasDouble = True
        # For words that are reverse of each other
        elif key[0] < key[1]:  # Only process each pair once
            rev = key[1] + key[0]  # Find the reverse word
            pal += min(val, freq[rev]) * 4  # Take the min count of both words and multiply by 4

    return pal + hasDouble * 2  # Add base palindrome length plus 2 if we can place a double-letter word in center


print(longPalin(words=["lc", "cl", "gg"]))
""""gg": 1 word with identical letters → contributes 0 pairs + center = 2 chars
    "lc"/"cl": 1 pair → contributes 4 chars
    Total: 4 + 2 = 6 characters ("lcggcl")"""
