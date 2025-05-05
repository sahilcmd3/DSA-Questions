# LEETCODE

"""Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from
magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote."""


# Time Complexity: O(m+n)
def canConstruct(ransomnote, magazine):
    freq_hash = {}

    for c in magazine:  # m
        freq_hash[c] = 1 + freq_hash.get(c, 0)

    for c in ransomnote:  # n
        if c not in freq_hash or freq_hash[c] <= 0:
            return False
        freq_hash[c] -= 1

    return True

print(canConstruct(ransomnote="aa", magazine="aab"))