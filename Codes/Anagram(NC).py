# NEETCODE

"""Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
An anagram is a string that contains the exact same characters as another string,
but the order of the characters can be different."""

def anagram(s, t):
    lst1 = list(s)
    lst2 = list(t)
    if len(lst1) != len(lst2):
        return False
    for i in range(len(lst1)):  #Time complexity: O(i) and space complexity= O(s+t)
        if lst1[i] not in lst2:
            return False
        lst2.remove(lst1[i])
    return True


s = "history"
t = "yistorh"
a = anagram(s, t)
print(a)