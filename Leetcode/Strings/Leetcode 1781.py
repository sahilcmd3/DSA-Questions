# Sum of Beauty of All Substrings

"""The beauty of a string is the difference in frequencies between the most frequent and least frequent characters.
    For example, the beauty of "abaacc" is 3 - 1 = 2.

Given a string s, return the sum of beauty of all of its substrings."""


from collections import Counter


# Time Complexity: O(n^2 * 26) {The max() and min() are performed over at most 26 elements (a–z), so they're constant time}
class Solution:
    def beautySum(self, s):
        total_beauty = 0

        for i in range(len(s)):
            freq = Counter()
            for j in range(i, len(s)):
                freq[s[j]] += 1
                total_beauty += max(freq.values()) - min(freq.values())

        return total_beauty


if __name__ == "__main__":
    obj = Solution()
    print(obj.beautySum(s="aabcb"))
