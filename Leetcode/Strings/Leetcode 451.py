# Sort Character by Frequency

"""Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is
the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them."""


# Time complexity: O(n logn)
class Solution:
    def freqSort(self, s: str) -> str:
        freq = {}

        for char in s:
            if char not in freq:
                freq[char] = 1
            else:
                freq[char] += 1

        res = ""
        for char, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            res += char * count

        return res


if __name__ == "__main__":
    obj = Solution()
    print(obj.freqSort(s="tree"))
