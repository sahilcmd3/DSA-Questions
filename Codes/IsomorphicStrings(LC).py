# LEETCODE

"""Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two
characters may map to the same character, but a character may map to itself."""


# Time Complexity: O(N)
def isIsomorphic(s,t):
    char_index_s={}  # Hashmap
    char_index_t={}

    for i in range(len(s)):  # Loop through s
        if s[i] not in char_index_s:  # For the character at index i in string s, the code checks if that character is
            # already a key in char_index_s. If it is not, it adds the character as a key and sets its value
            # to the current index i. This records the first occurrence of the character in s.
            char_index_s[s[i]]=i

        if t[i] not in char_index_t:  # Same
            char_index_t[t[i]]=i

        if char_index_s[s[i]]!=char_index_t[t[i]]:  # The code checks whether the index of the current character from s
            # in char_index_s matches the index of the corresponding character from t in char_index_t. If they do not
            # match, it means that the characters are not isomorphic (i.e., they do not maintain the same character
            # mapping), so the function returns False.

            return False

    return True

print(isIsomorphic(s="egg", t="add"))