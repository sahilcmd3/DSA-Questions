#LEETCODE

"""Given a string s consisting of words and spaces, return the length of the last word in the string.
A word is a maximal substring consisting of non-space characters only.
A substring is a contiguous non-empty sequence of characters within a string."""

def length_last_word(s):
    return len(s.split()[-1]) #splits and removes white spaces

s="Hello world  "
ans=length_last_word(s)
print(ans)