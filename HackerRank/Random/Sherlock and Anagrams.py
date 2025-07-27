"""Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string.
Given a string, find the number of pairs of substrings of the string that are anagrams of each other.
"""


def sherlockAndAnagram(s):
    substring_freq = {}
    n = len(s)

    for length in range(1, n):
        for i in range(n - length + 1):
            substring = "".join(sorted(s[i : i + length]))

            if substring in substring_freq:
                substring_freq[substring] += 1
            else:
                substring_freq[substring] = 1

    count = 0
    for freq in substring_freq.values():
        count += (freq * (freq - 1)) // 2

    return count


if __name__ == "__main__":
    print(sherlockAndAnagram(s="mom"))
