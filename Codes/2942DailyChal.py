# Leetcode

"""You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.

Example 1:

Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1."""


# Time complexity: O(n*m)
# m is the average length of the words.
# n is the number of words in the list.
def findwords(words,x):
    return [i for i in range (len(words)) if x in words[i]]

print(findwords(words = ["leet","code"], x = "e"))