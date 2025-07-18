# LEETCODE

"""Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. 

Specifically:  
    Each letter in pattern maps to exactly one unique word in s.
    Each unique word in s maps to exactly one letter in pattern.
    No two letters map to the same word, and no two words map to the same letter."""


def wordPattern(pattern,s):
        l = s.split(" ")

        if len(l)!=len(pattern):
            return False

        d ={}
        se=set()

        for i in range(len(pattern)):
            if pattern[i] in d:
                if d[pattern[i]]!=l[i]:
                    return False
            else:
                if l[i] not in se:
                    d[pattern[i]]=l[i]
                    se.add(l[i])
                else:
                    return False
        
        return True


print(wordPattern(pattern = "abba", s = "dog cat cat dog"))