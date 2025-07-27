#LEETCODE (Hard)

"""Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that
every character in t (including duplicates) is included in the window. If there is no such substring, return the
empty string "".

The testcases will be generated such that the answer is unique."""


from collections import defaultdict
"""provides a default value for a key that does not exist in the dictionary, eliminating the need to check for the 
key's existence before accessing or modifying it."""


# Time Complexity: O(s+t)
def minWindow(s, t):
    if len(s) < len(t):  # If target is greater than s
        return ""

    char_count = defaultdict(int)  # Creating a char_count dictionary using defaultdict(int) to store the frequency of
    # each character in t. Initialize all counts to 0 by default.
    for ch in t:  # Looping through each character in t and increment its count in char_count
        char_count[ch] = 1

    target_chars_rem = len(t)  # tracking how many characters from t are still needed in the current window.
    # Initially, it's set to the length of t
    min_window = (0, float('inf'))  # holds the start and end indices of the smallest window found. Initialize with
    # (0, float("inf")), indicating no valid window found yet
    start_index = 0  # is the beginning of the current window in s

    for end_index, ch in enumerate(s):  # Iterate through s using end_index as the index and ch as the character
        if char_count[ch] > 0:  # If ch is a required character (its count in char_count is positive), decrement
            # target_chars_remaining because one more required character is included.
            target_chars_rem -= 1
        char_count[ch] -= 1  # Decrease the count of ch in char_count because it's now part of the window

        if target_chars_rem == 0:  # When target_chars is 0, it means the current window contains all required characters
            # Start contracting the window from the left by moving start_index to the right:
            # Get the character at start_index.
            # If its count in char_count is 0, exit the loop because it means this character is needed for a valid window
            # Otherwise, increment its count and move start_index to the right to shrink the window.
            while True:
                char_at_start = s[start_index]
                if char_count[char_at_start] == 0:
                    break
                char_count[char_at_start] += 1
                start_index += 1

            if end_index - start_index < min_window[1] - min_window[0]:  # After contracting the window, check if
                # the current window is smaller than the previously found minimum window.
                min_window = (start_index, end_index)  # update min_window to the new start and end indices.

            char_count[s[start_index]] += 1  # After finding a valid window and updating min_window, adjust the
            # character count for the character being removed from the window (s[start_index]).
            target_chars_rem += 1  # Increasing since a required character is no longer in the window.
            start_index += 1  # Moving start_index to the right to continue searching for smaller windows.

    return "" if min_window[1] > len(s) else s[min_window[0]:min_window[1] + 1]
    # After iterating through s, check if a valid window was found.
    # If min_window[1] is still float("inf"), no valid window was found, so return an empty string.
    # Otherwise, return the smallest window substring from s using the indices stored in min_window.


ans = minWindow(s="ADOBECODEBANC", t="ABC")
print(ans)
