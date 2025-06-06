# LEETCODE (medium)


"""You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence relation:

Reflexivity: 'a' == 'a'.
Symmetry: 'a' == 'b' implies 'b' == 'a'.
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed",
and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.
"""


class UnionFind:
    def __init__(self, N):
        self.root = list(range(N))

    def Find(self, x):
        if self.root[x] != x:
            self.root[x] = self.Find(self.root[x])  # Path compression
        return self.root[x]

    def Union(self, x, y):
        x_root = self.Find(x)
        y_root = self.Find(y)

        if x_root != y_root:
            # Always point to the smaller character to maintain lexicographical order
            if x_root < y_root:
                self.root[y_root] = x_root
            else:
                self.root[x_root] = y_root


class Solution:
    def smallestEquivalentString(self, s1, s2, baseStr):
        G = UnionFind(26)
        n = len(s1)

        for i in range(n):
            G.Union(ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a'))

        ans = ""
        for x in baseStr:
            ans += chr(G.Find(ord(x) - ord('a')) + ord('a'))

        return ans


obj = Solution()
print(obj.smallestEquivalentString(s1="parker", s2="morris", baseStr="parser"))
