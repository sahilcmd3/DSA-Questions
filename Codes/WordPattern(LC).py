"""Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Specifically:
    Each letter in pattern maps to exactly one unique word in s.
    Each unique word in s maps to exactly one letter in pattern.
    No two letters map to the same word, and no two words map to the same letter.

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Explanation:
The bijection can be established as:
'a' maps to "dog".
'b' maps to "cat"."""


# Time complexity: O(s)
def wordPattern(pattern, s):
    l = s.split(" ")  # converts the string into a list of words

    if len(l) != len(pattern):  # check whether the length of list L and pattern are the same or not;
        # if not, it's not possible to match
        return False

    d = {}  # for mapping of characters to words
    se = set()  # to keep track of words already marked

    for i in range(len(pattern)):  # iterate through the length of pattern, and now let's see whether pattern [i]
        # is in dict d; if yes, then check whether it has already been matched to the same; if not, return False
        if pattern[i] in d:
            if d[pattern[i]] != l[i]:
                return False
        else:
            if l[i] not in se:  # If the character is not in d, ensure the word isn't already mapped to another
                # character (using se). If the word is free, map it to the character and add it to se.
                d[pattern[i]] = l[i]
                se.add(l[i])
            else:  # If not, return False
                return False

    return True


print(wordPattern(pattern="abba", s="dog cat cat dog"))