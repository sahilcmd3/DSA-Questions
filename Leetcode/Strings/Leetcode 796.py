# Rotate String

"""Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
    For example, if s = "abcde", then it will be "bcdea" after one shift."""


# Time Complexity: O(n)
class Solution:
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        
        doubled = s + s  # Any rotation of s appears as a contiguous substring of s+s

        return goal in doubled  # s = "abcde", goal = "cdeab" doubled = "abcdeabcde", and "cdeab" is a substring → returns True.


if __name__ == "__main__":
    obj = Solution()
    print(obj.rotateString(s="abcde", goal="cdeab"))
