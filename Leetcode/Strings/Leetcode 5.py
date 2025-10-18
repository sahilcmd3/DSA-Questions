# Longest Palindromic Substring

"""Given a string s, return the longest palindromic substring in s."""


# Time Complexity: O(n^2)
class Solution:
    def palin_aroud_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1

    def longestSubstr(self, s):
        if not s:
            return ""

        start = 0
        end = 0

        for i in range(len(s)):
            odd = self.palin_aroud_center(s, i, i)
            even = self.palin_aroud_center(s, i, i + 1)
            max_len = max(odd, even)

            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2

        return s[start : end + 1]


if __name__ == "__main__":
    obj = Solution()
    print(obj.longestSubstr(s="cbbd"))
