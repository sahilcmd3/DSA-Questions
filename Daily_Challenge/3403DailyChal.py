# LEETCODE (medium)


"""You are given a string word, and an integer numFriends.

Alice is organizing a game for her numFriends friends. There are multiple rounds in the game, where in each round:
    word is split into numFriends non-empty strings, such that no previous round has had the exact same split.
    All the split words are put into a box.

Find the lexicographically largest string from the box after all the rounds are finished.

Lexicographically Smaller: A string a is lexicographically smaller than a string b if in the first position where a and b differ,
string a has a letter that appears earlier in the alphabet than the corresponding letter in b. If the first min(a.length, b.length)
characters do not differ, then the shorter string is the lexicographically smaller one.
"""


# Time Complexity: O(n*k) where k is the substring length.
def answerString(word, numFriends):
    if numFriends == 1:
        return word

    n = len(word)
    length = n - numFriends + 1
    max_char = max(word)
    result = ""

    for i in range(n):
        if word[i] == max_char:
            substr = word[i : i + length]
            result = max(result, substr)

    return result


print(answerString(word="dbca", numFriends=2))
