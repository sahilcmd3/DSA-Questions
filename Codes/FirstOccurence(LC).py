#LEETCODE

"""Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0."""

#Time complexity: O(n)
def strStr(haystack, needle):

    if len(haystack)<len(needle):
        return -1

    for i in range(len(haystack)):
        if haystack[i:i+len(needle)]==needle:
            return i
        else:
            return -1

ans=strStr(haystack="hello",needle = "ll")
print(ans)


#KMP Matcher
#Time complexity: O(m+n)
def kmp_search(haystack, needle):
    def compute_lps(pattern):
        # Create the "longest prefix suffix" (LPS) array
        lps = [0] * len(pattern)
        length = 0  # Length of previous longest prefix suffix
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    if not needle:
        return 0  # Empty needle is always found at index 0

    # Preprocess the needle to get the LPS array
    lps = compute_lps(needle)

    i = 0  # Index for haystack
    j = 0  # Index for needle

    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1

        if j == len(needle):  # Full match found
            return i - j

        elif i < len(haystack) and haystack[i] != needle[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1  # Needle not found in haystack


result = kmp_search(haystack = "hello",needle = "ll")
print(result)