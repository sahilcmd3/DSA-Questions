# LEETCODE (medium)

"""Given an array of strings strs, group the anagrams together. You can return the answer in any order."""


# Time complexity: O([n*n]*k)
"""def ana(s, t):  # Checks for anagram
    if len(s) != len(t):
        return False

    s_count = {}
    t_count = {}

    for i in range(len(s)):
        s_count[s[i]] = 1 + s_count.get(s[i], 0)
        t_count[t[i]] = 1 + t_count.get(t[i], 0)

    return s_count == t_count


def group(strs):  #ana function called here to check and then group the same type of anagram
    grp_ana = []
    visited = set()

    for i in range(len(strs)):
        if strs[i] in visited:
            continue

        curr_group = [strs[i]]
        visited.add(strs[i])

        for j in range(i + 1, len(strs)):
            if ana(strs[i], strs[j]):
                curr_group.append(strs[j])
                visited.add(strs[j])

        grp_ana.append(curr_group)

    return grp_ana


print(group(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))"""


# Time complexity: O(m∗nlogn)
from collections import defaultdict
# Optimal Approach
def group(strs):
    ans= defaultdict(list)  # created with list as the default factory. This means that if 
    # a key does not exist in the dictionary, it automatically creates an empty list for that key.

    for s in strs:
        # The string s is sorted alphabetically using the sorted() function. Sorting rearranges the 
        # characters of the string in a defined order (lexicographical order).
        # The sorted characters are then joined back together to form a new string (key).
        # This sorted string (key) acts as a unique identifier for anagrams. For example, both "eat" 
        # and "tea" will produce the key "aet".
        key = "".join(sorted(s))
        ans[key].append(s)
    
    return list(ans.values())
print(group(strs=["eat", "tea", "tan", "ate", "nat", "bat"]))