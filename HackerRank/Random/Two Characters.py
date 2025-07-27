"""Given a string, remove characters until the string is made up of any two alternating characters. When you choose a character to
remove, all instances of that character must be removed. Determine the longest string possible that contains just two alternating letters.

Example
s = 'abaacdabd'

Delete a, to leave bcdbd. Now, remove the character c to leave the valid string bdbd with a length of 4. Removing either b or d at
any point would not result in a valid string. Return 4.

Given a string s, convert it to the longest possible string t made up only of alternating characters. Return the length of string t.
If no string t can be formed, return 0."""


class Solution:
    def isConsecutive(self, st):
        if len(st) < 2:
            return True

        for i in range(1, len(st)):
            if st[i] == st[i - 1]:
                return True

        return False

    def alternate(self, s):
        chars = list(set(s))
        candidates = []
        maxalter = float("-inf")

        for i in range(len(chars) - 1):
            for j in range(i + 1, len(chars)):
                candidates.append([chars[i], chars[j]])

        for candi in candidates:
            temp = ""
            for c in s:
                if c in candi:
                    temp += c

            if not self.isConsecutive(temp):
                maxalter = max(maxalter, len(temp))

        return maxalter if maxalter != float("inf") else 0


if __name__ == "__main__":
    obj = Solution()
    print(obj.alternate(s="abaacdabd"))
