# LEETCODE

"""Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string"""


# Time Complexity: O(N*M)
def longest_common_prefix(strs):

    pref = strs[0]
    pref_len = len(pref)

    for s in strs[1:]:
        """Check if the current string s matches with the current prefix pref. If not, 
           reduce the length of the prefix pref_len by 1 and update the prefix accordingly until it matches with s"""
        while pref != s[0:pref_len]:
            pref_len -= 1
            if pref_len == 0:
                return ""

            pref = pref[0:pref_len]

    return pref


strs = ["reflower", "flow", "flight"]
ans = longest_common_prefix(strs)
print(ans)