# NEETCODE & LEETCODE

"""Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string,
but the order of the characters can be different."""

"""def anagram(s, t):
    lst1 = list(s)
    lst2 = list(t)
    if len(lst1) != len(lst2):
        return False
    for i in range(len(lst1)):  #Time complexity: O(i) and space complexity= O(s+t)
        if lst1[i] not in lst2:
            return False
        lst2.remove(lst1[i])
    return True"""


# Hashmap
# Time complexity: O(n)
def anagram(s, t):
    if len(s) != len(t):
        return False

    s_count = {}
    t_count = {}

    for i in range(len(s)):
        # Counted and compared characters in hashmaps
        s_count[s[i]] = 1 + s_count.get(s[i], 0)
        t_count[t[i]] = 1 + t_count.get(t[i], 0)

    return s_count==t_count


print(anagram(s="history", t="yistorh"))