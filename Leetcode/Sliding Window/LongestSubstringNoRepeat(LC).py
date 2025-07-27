#LEETCODE (medium)

"""Given a string s, find the length of the longest substring without duplicate characters."""


# Time Complexity: O(n)
def longest(s):
    max_length = 0  # Length of the longest substring without repeating characters found
    left = 0  # Left part of window
    count = {}  # Hashmap

    for right, c in enumerate(s):  # Enum returns both index and characters of the c (char at curr_index)
        count[c] = 1 + count.get(c, 0)  # Add 1 if c not present else increment

        while count[c] > 1:
            count[s[left]] -= 1  # Decrease the count  of left if no repeating char is found in map
            left += 1  # Increment the value in s

        max_length = max(max_length, right - left + 1)  # Calculate and compare length of window if big replace it

    return max_length


ans = longest(s="abcabcbb")
print(ans)