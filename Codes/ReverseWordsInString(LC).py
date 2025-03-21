#LEETCODE (medium)

"""Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should
only have a single space separating the words. Do not include any extra spaces."""

#Time Complexity: O(n)
def reverse_words(s):

    words=s.split()
    res=[]

    for i in range(len(words)-1,-1,-1):
        res.append(words[i])
        if i!=0:
            res.append(" ")

    return "".join(res)

s = "the sky is blue"
ans=reverse_words(s)
print(ans)


#other method
"""
def reverse_words(s):
    s=s.split()
    s=s[::-1]
    s=" ".join(s)
    return s
"""