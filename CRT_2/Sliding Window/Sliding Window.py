# Dynamic Sliding Window
"""Window increases or decreases
Template:
    int n = s.size();
    int left = 0;
    int ans = 0;

    for (int right = 0; right < n; right++)

        // use nums[right] sum+=nums[right]
        // jab cheezein allow nhi hoti toh while loop chalega
        // while/if (window_size / requirement > 1)
        // left ko remove krdo and left++"""


# LEETCODE 3
"""Given a string s, find the length of the longest substring without duplicate characters."""


# Time Complexity: O(n)
def lenOfSub(s):
    n = len(s)
    left = 0
    ans = 0
    dict = {}

    for right in range(n):
        if (
            s[right] not in dict
        ):  # We can use dict's inbuilt function .get that checks if present add 1 else increase from 0
            dict[s[right]] = 0
        dict[s[right]] += 1

        while dict[s[right]] > 1:
            dict[s[left]] -= 1
            if dict[s[left]] == 0:
                del dict[s[left]]

            left += 1

        ans = max(ans, right - left + 1)

    return ans


if __name__ == "__main__":
    print(lenOfSub(s="abcabcbb"))
